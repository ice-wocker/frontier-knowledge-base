#!/usr/bin/env python3
"""把 docs/ 下的 Markdown 渲染成一套静态站点（GitHub Pages）。

为什么要站点：163 篇文档全在 docs/ 里躺着，发现成本极高——没有检索、
没有目录页、没有「上一篇/下一篇」。内容质量已经够了，缺的只是形式。

设计取舍：
- 零依赖：不引入 MkDocs / VitePress，只用标准库。构建产物是纯静态 HTML，
  克隆下来双击 index.html 就能看，也方便以后换任何托管。
- 不碰原文：Markdown 是唯一真相源，站点只是投影；改内容只改 docs/。
- 检索用倒排索引 + BM25（见 scripts/kb.py），不再把正文全塞进 JSON。
  首屏 0 请求，第一次输入才拉索引；单次按键只查候选集而非全库扫描。

除了渲染，本脚本还顺带产出知识库的「机器可读形态」：
    search-index.json  倒排索引（浏览器端检索）
    docs.json          全部文档的元数据 + 摘要 + 标签 + 相关文档（可被程序消费）
    graph.json         文档关联图（节点 + 边，给可视化/分析用）
    tags.json          标签 -> 文档 的聚合
    feed.xml           RSS（按更新时间）
    sitemap.xml / robots.txt
"""
import argparse
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

import kb
from kb import DOCS, DOMAINS, ROOT

OUT = ROOT / "site"
DOMAIN_ORDER = kb.DOMAIN_ORDER
DOMAIN_LABEL = kb.DOMAIN_LABEL
# 站点当前的对外地址。换域名只改这一处 + kb 无关。
SITE_URL = "https://ice-wocker.github.io/frontier-knowledge-base"


# ---------- Markdown 渲染（只覆盖本仓库实际用到的子集） ----------

def esc(s):
    return html.escape(s, quote=False)


def slugify(text):
    return re.sub(r'[^\w\u4e00-\u9fff]+', '-', text).strip('-').lower()


def inline(text):
    """行内元素：先转义，再处理 code / 粗体 / 链接，顺序不能反。"""
    text = esc(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

    def link(m):
        label, url = m.group(1), m.group(2)
        ext = url.startswith('http')
        attrs = ' target="_blank" rel="noopener noreferrer"' if ext else ''
        return f'<a href="{url}"{attrs}>{label}</a>'

    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, text)
    return text


def render_markdown(md):
    """渲染正文，同时收集 H2/H3 作为目录（TOC）。返回 (html, toc)。"""
    lines = md.split('\n')
    out, toc = [], []
    i = 0
    in_ul = in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append('</ul>'); in_ul = False
        if in_ol:
            out.append('</ol>'); in_ol = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # 表格：连续的 | 开头的行
        if stripped.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            close_lists()
            header = [c.strip() for c in stripped.strip('|').split('|')]
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            out.append('<div class="table-wrap"><table>')
            out.append('<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in header) + '</tr></thead>')
            out.append('<tbody>')
            for r in rows:
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            out.append('</tbody></table></div>')
            continue

        if not stripped:
            close_lists()
            i += 1
            continue

        m = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if m:
            close_lists()
            level = len(m.group(1))
            text = m.group(2).strip()
            if level == 1:
                i += 1  # H1 由模板负责，正文里跳过（避免重复）
                continue
            anchor = slugify(text)
            # 锚点去重：同页同名标题加后缀
            base, n = anchor, 1
            while anchor in [t[2] for t in toc]:
                n += 1
                anchor = f"{base}-{n}"
            if level == 2:
                toc.append((level, text, anchor))
            out.append(f'<h{level} id="{anchor}">{inline(text)}</h{level}>')
            i += 1
            continue

        if stripped.startswith('>'):
            close_lists()
            quote = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote.append(lines[i].strip().lstrip('>').strip())
                i += 1
            out.append('<blockquote>' + ' '.join(inline(q) for q in quote if q) + '</blockquote>')
            continue

        if re.match(r'^([-*+])\s+', stripped):
            if not in_ul:
                close_lists(); out.append('<ul>'); in_ul = True
            out.append('<li>' + inline(re.sub(r'^([-*+])\s+', '', stripped)) + '</li>')
            i += 1
            continue

        if re.match(r'^\d+\.\s+', stripped):
            if not in_ol:
                close_lists(); out.append('<ol>'); in_ol = True
            out.append('<li>' + inline(re.sub(r'^\d+\.\s+', '', stripped)) + '</li>')
            i += 1
            continue

        close_lists()
        out.append('<p>' + inline(stripped) + '</p>')
        i += 1

    close_lists()
    return '\n'.join(out), toc


def plain_text(md):
    """Markdown -> 纯文本（做摘要用）。"""
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    t = re.sub(r'[#>|*`]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def summary_of(text, limit=180):
    m = re.search(r'^##\s+概述\s*$', text, re.M)
    body = text[m.end():] if m else text
    s = plain_text(body)
    return (s[:limit] + '…') if len(s) > limit else s


# ---------- 模板 ----------

CSS = """
:root{--bg:#0d1117;--panel:#161b22;--border:#30363d;--fg:#e6edf3;--muted:#8b949e;
--accent:#58a6ff;--accent2:#7ee787}
@media(prefers-color-scheme:light){:root{--bg:#fff;--panel:#f6f8fa;--border:#d0d7de;
--fg:#1f2328;--muted:#59636e;--accent:#0969da;--accent2:#1a7f37}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
-webkit-text-size-adjust:100%}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header.top{position:sticky;top:0;background:color-mix(in srgb,var(--bg) 92%,transparent);
backdrop-filter:blur(8px);border-bottom:1px solid var(--border);z-index:10}
.wrap{max-width:900px;margin:0 auto;padding:0 20px}
header.top .wrap{display:flex;align-items:center;gap:14px;height:56px}
header.top .brand{font-weight:600;white-space:nowrap}
header.top .brand em{color:var(--accent2);font-style:normal}
header.top .spacer{flex:1}
header.top a.ic{color:var(--muted);font-size:.9rem}
nav.domains{display:flex;gap:8px;overflow-x:auto;padding:10px 0;font-size:14px;
border-bottom:1px solid var(--border);scrollbar-width:thin}
nav.domains a{color:var(--muted);white-space:nowrap;padding:3px 9px;border-radius:6px}
nav.domains a.active,nav.domains a:hover{color:var(--fg);background:var(--panel);text-decoration:none}
main{padding:28px 0 80px}
h1{font-size:1.7rem;line-height:1.35;margin:.2em 0 .6em}
h2{font-size:1.25rem;margin:1.8em 0 .6em;padding-top:.6em;border-top:1px solid var(--border)}
h3{font-size:1.05rem;margin:1.4em 0 .5em}
blockquote{margin:0 0 1.2em;padding:.6em 1em;border-left:3px solid var(--accent);
background:var(--panel);color:var(--muted);border-radius:0 8px 8px 0;font-size:.92rem}
code{background:var(--panel);padding:.15em .4em;border-radius:5px;font-size:.88em;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:var(--panel);padding:14px;border-radius:8px;overflow-x:auto;border:1px solid var(--border)}
pre code{background:none;padding:0}
.table-wrap{overflow-x:auto;margin:1em 0;border:1px solid var(--border);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{padding:8px 12px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top}
th{background:var(--panel);font-weight:600;white-space:nowrap}
tr:last-child td{border-bottom:none}
ul,ol{padding-left:1.4em}
li{margin:.3em 0}
.meta{color:var(--muted);font-size:.88rem;margin-bottom:1.6em}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin:1em 0 1.6em}
.card{display:block;padding:14px 16px;background:var(--panel);border:1px solid var(--border);
border-radius:10px;color:var(--fg)}
.card:hover{border-color:var(--accent);text-decoration:none}
.card .t{font-weight:600;margin-bottom:6px}
.card .d{color:var(--muted);font-size:.82rem}
.crumb{font-size:.88rem;color:var(--muted);margin-bottom:1.2em}
.hero{padding:8px 0 4px}
.hero h1{margin:.1em 0 .3em}
.hero p{color:var(--muted);margin:0 0 1em}
.stats{display:flex;gap:20px;flex-wrap:wrap;margin:1.2em 0 1.6em;color:var(--muted);font-size:.9rem}
.stats b{color:var(--fg);font-size:1.3rem;display:block}
.searchbox{width:100%;padding:11px 14px;border-radius:10px;border:1px solid var(--border);
background:var(--panel);color:var(--fg);font-size:1rem}
.searchbox:focus{outline:none;border-color:var(--accent)}
#results{margin-top:13px}
.hit{display:block;padding:10px 12px;border:1px solid var(--border);border-radius:8px;
margin-bottom:8px;color:var(--fg)}
.hit:hover{border-color:var(--accent);text-decoration:none}
.hit .d{color:var(--muted);font-size:.8rem}
.hit mark{background:#3d2f00;color:#ffd76e;border-radius:3px;padding:0 2px}
@media(prefers-color-scheme:light){.hit mark{background:#fff8c5;color:#7d4e00}}
footer{border-top:1px solid var(--border);color:var(--muted);font-size:.85rem;padding:22px 0 40px}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:3em;
padding-top:1.4em;border-top:1px solid var(--border);font-size:.9rem}
.pager a{max-width:48%}
.toc{background:var(--panel);border:1px solid var(--border);border-radius:10px;
padding:12px 18px;margin:0 0 1.8em;font-size:.9rem}
.toc summary{cursor:pointer;color:var(--muted);font-weight:600;user-select:none}
.toc ol{margin:.7em 0 .2em;padding-left:1.3em}
.toc li{margin:.25em 0}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:.8em 0 1.4em}
.chip{font-size:.78rem;color:var(--muted);background:var(--panel);border:1px solid var(--border);
padding:2px 9px;border-radius:999px}
a.chip:hover{color:var(--accent);border-color:var(--accent);text-decoration:none}
.rel{margin-top:2.6em;padding-top:1.2em;border-top:1px solid var(--border)}
.rel h2{border:0;padding-top:0;font-size:1.05rem;margin-top:.2em}
.tagcloud{display:flex;flex-wrap:wrap;gap:8px;margin:1.2em 0}
@media(max-width:600px){h1{font-size:1.4rem}.wrap{padding:0 16px}.toc{font-size:.85rem}}
"""

SEARCH_JS = r"""
(function(){
  var box=document.getElementById('q'), out=document.getElementById('results');
  if(!box) return;
  var idx=null, meta=null, pending=null;
  function load(){
    if(pending) return pending;
    pending=Promise.all([
      fetch('search-index.json').then(function(r){return r.json()}),
      fetch('docs.json').then(function(r){return r.json()})
    ]).then(function(a){idx=a[0];meta=a[1];});
    return pending;
  }
  var CJK=/[\u4e00-\u9fff]/;
  function tokenize(text){
    text=text.toLowerCase(); var out=[]; var re=/[\u4e00-\u9fff]+|[a-z][a-z0-9+#._-]*|\d+/g,m;
    while((m=re.exec(text))){
      var t=m[0];
      if(CJK.test(t)){ if(t.length===1){out.push(t);} else {for(var i=0;i<t.length-1;i++)out.push(t.substr(i,2));} }
      else if(/^\d+$/.test(t)){out.push(t);}
      else if(t.length>=2){out.push(t);}
    }
    return out;
  }
  function render(kw){
    if(!idx||!meta) return;
    kw=kw.trim().toLowerCase();
    if(!kw){out.innerHTML='';return;}
    var terms=tokenize(kw); if(!terms.length){out.innerHTML='';return;}
    var qc={}, scores={}, P=idx.p, names=meta.docs;
    for(var i=0;i<terms.length;i++){qc[terms[i]]=(qc[terms[i]]||0)+1;}
    var dl=idx.dl, avgdl=idx.avgdl||1, k1=1.5, b=0.75;
    for(var t in qc){
      var p=P[t]; if(!p) continue;
      var w=idx.idf[t]*(1+Math.log(qc[t]));
      for(var key in p){
        var i=+key, tf=p[key];
        var denom=tf+k1*(1-b+b*((dl[i]||avgdl)/avgdl));
        scores[i]=(scores[i]||0)+w*(tf*(k1+1))/(denom||1);
      }
    }
    var arr=[];
    for(var i in scores){
      var i2=+i, title=names[i2].t.toLowerCase();
      for(var t2 in qc){ if(title.indexOf(t2)>=0) scores[i2]+=3*idx.idf[t2]; }
      arr.push([scores[i2], i2]);
    }
    arr.sort(function(a,b){return b[0]-a[0]});
    arr=arr.slice(0,40);
    if(!arr.length){out.innerHTML='<p class="meta">没有匹配的文档。</p>';return;}
    out.innerHTML=arr.map(function(h){
      var d=names[h[1]], s=d.s||'';
      for(var i=0;i<terms.length;i++){
        var re=new RegExp('('+terms[i].replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig');
        s=s.replace(re,'<mark>$1</mark>');
      }
      return '<a class="hit" href="'+d.u+'"><div>'+d.t+'</div><div class="d">'+d.dm+(d.ud?' · '+d.ud:'')+' · '+d.rm+' 分钟</div><div class="d">'+s+'</div></a>';
    }).join('');
  }
  box.addEventListener('input',function(){
    if(!idx){ load().then(function(){render(box.value)}); } else { render(box.value); }
  });
  box.addEventListener('focus',load,{once:true});
})();
"""


def page(title, body, depth, active_slug=None, search=False, desc=None, canonical=None):
    prefix = '../' * depth
    nav = ''.join(
        f'<a class="{"active" if s == active_slug else ""}" href="{prefix}{s}/index.html">{html.escape(l)}</a>'
        for s, l in DOMAINS
    )
    nav = f'<a class="{"active" if active_slug == "all" else ""}" href="{prefix}index.html">全部</a>' + nav
    desc = desc or f"前沿科技知识库 · {title}"
    canon = canonical or f"{SITE_URL}/{'../' * depth}".rstrip('/') + '/'
    depth_script = f'<script>{SEARCH_JS}</script>' if search else ''
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0d1117">
<link rel="canonical" href="{html.escape(canon)}">
<link rel="alternate" type="application/rss+xml" title="前沿科技知识库" href="{prefix}feed.xml">
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
<header class="top"><div class="wrap"><span class="brand">🧊 <em>前沿科技</em>知识库</span>
<span class="spacer"></span>
<a class="ic" href="{prefix}index.html">首页</a>
<a class="ic" href="{prefix}tags.html">标签</a>
<a class="ic" href="{prefix}feed.xml">RSS</a>
</div>
<nav class="domains"><div class="wrap">{nav}</div></nav></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
内容基于公开网络资料整理，逐条附来源链接；不对来源准确性作担保，请以官方一手信息为准。<br>
<a href="https://github.com/ice-wocker/frontier-knowledge-base">在 GitHub 上查看源仓库</a> ·
<a href="{prefix}docs.json">docs.json</a> ·
<a href="{prefix}search-index.json">search-index.json</a> ·
<a href="{prefix}graph.json">graph.json</a>
</div></footer>
{depth_script}
</body>
</html>"""


def card(d, href, extra=""):
    return (f'<a class="card" href="{href}"><div class="t">{html.escape(d["title"])}</div>'
            f'<div class="d">{d["updated"]}{extra}</div></a>')


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / 'style.css').write_text(CSS, encoding='utf-8')

    docs = kb.load_docs()
    index = kb.build_index(docs)

    # ---- 每篇的派生数据：摘要 / 标签 / 相关 / 阅读时长 ----
    enriched = []
    for i, d in enumerate(docs):
        body_html, toc = render_markdown(d['text'])
        rel = [(docs[j]['title'], docs[j]['domain_slug'], docs[j]['stem'], s)
               for j, s in kb.related(docs, index, i)]
        enriched.append({
            **d,
            'body': body_html,
            'toc': toc,
            'summary': summary_of(d['text']),
            'tags': kb.tags_for(d, index, docs),
            'related': rel,
            'read_min': kb.reading_minutes(d['text']),
            'refs': kb.extract_refs(d['text']),
            'url': f"{d['domain_slug']}/{d['stem']}.html",
        })

    by_domain: dict[str, list[dict]] = {}
    for d in enriched:
        by_domain.setdefault(d['domain_slug'], []).append(d)

    # ---- 检索索引（倒排，浏览器端 BM25）----
    # 扁平化 postings：{term: [docId, tf, docId, tf, ...]}。
    # 比 {term:{docId:tf}} 省约 20% 体积，JSON 解析也更快。
    postings = {}
    for term, pl in index['postings'].items():
        flat = []
        for k, v in pl.items():
            flat.append(k); flat.append(v)
        postings[term] = flat
    search_index = {
        'avgdl': (sum(index['dl']) / len(index['dl'])) if index['dl'] else 1,
        'dl': index['dl'],
        'p': postings,
        'idf': {k: round(v, 4) for k, v in index['idf'].items()},
    }
    (OUT / 'search-index.json').write_text(
        json.dumps(search_index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

    # ---- docs.json：机器可读的文档清单 ----
    docs_json = {
        'generated': date.today().isoformat(),
        'site': SITE_URL,
        'count': len(enriched),
        'docs': [{
            'i': i,
            'title': d['title'],
            't': d['title'],
            'u': d['url'],
            's': d['summary'],
            'dm': d['domain'],
            'd': d['domain_slug'],
            'ud': d['updated'],
            'rm': d['read_min'],
            'tags': d['tags'],
            'sections': d['sections'],
            'refs': len(d['refs']),
            'related': [{'title': t, 'url': f"{s}/{st}.html", 'score': round(sc, 4)}
                        for t, s, st, sc in d['related']],
        } for i, d in enumerate(enriched)],
    }
    (OUT / 'docs.json').write_text(
        json.dumps(docs_json, ensure_ascii=False, indent=1), encoding='utf-8')

    # ---- graph.json：关联图 ----
    graph = {
        'nodes': [{'id': i, 'label': d['title'], 'domain': d['domain_slug'],
                   'domain_label': d['domain'], 'url': d['url'],
                   'read_min': d['read_min'], 'refs': len(d['refs'])}
                  for i, d in enumerate(enriched)],
        'edges': [{'source': i, 'target': docs.index(next(x for x in docs if x['title'] == t
                                                          and x['domain_slug'] == s)),
                   'weight': round(sc, 4)}
                  for i, d in enumerate(enriched)
                  for t, s, st, sc in d['related']],
    }
    (OUT / 'graph.json').write_text(
        json.dumps(graph, ensure_ascii=False, indent=1), encoding='utf-8')

    # ---- tags.json ----
    tag_map: dict[str, list[str]] = {}
    for d in enriched:
        for t in d['tags']:
            tag_map.setdefault(t, []).append(d['url'])
    (OUT / 'tags.json').write_text(
        json.dumps(tag_map, ensure_ascii=False, indent=1), encoding='utf-8')

    # ---- 首页 ----
    sections = []
    for slug, label in DOMAINS:
        items = by_domain.get(slug, [])
        if not items:
            continue
        cards = ''.join(card(d, f'{slug}/{d["stem"]}.html', f' · {d["read_min"]} 分钟') for d in items)
        sections.append(f'<h2 id="{slug}">{html.escape(label)}（{len(items)} 篇）</h2>'
                        f'<div class="cards">{cards}</div>')
    total_refs = sum(len(d['refs']) for d in enriched)
    body = f"""<div class="hero">
<h1>前沿科技知识库</h1>
<p>覆盖 AI、硬件半导体、软件工程、数据工程、网络安全、基础科学、新兴科技、产业与社会。
内容基于公开网络资料整理，关键事实就地标注来源，每篇文末附完整链接清单，可逐条回溯。</p>
</div>
<div class="stats">
<div><b>{len(enriched)}</b>篇文档</div>
<div><b>{len(by_domain)}</b>个领域</div>
<div><b>{total_refs}</b>条来源链接</div>
<div><b>0</b>个第三方依赖</div>
</div>
<input id="q" class="searchbox" type="search" placeholder="搜索 {len(enriched)} 篇文档（BM25 全文检索）…" autocomplete="off" aria-label="搜索文档">
<div id="results" aria-live="polite"></div>
""" + '\n'.join(sections)
    (OUT / 'index.html').write_text(
        page('前沿科技知识库', body, 0, 'all', search=True,
             desc=f"前沿科技知识库：{len(enriched)} 篇专题文档，覆盖 AI、硬件、软件、数据、安全、科学、新兴科技等九大领域，逐条附来源链接。",
             canonical=f'{SITE_URL}/index.html'), encoding='utf-8')

    # ---- 领域页 ----
    for slug, label in DOMAINS:
        items = by_domain.get(slug, [])
        if not items:
            continue
        (OUT / slug).mkdir(exist_ok=True)
        cards = ''.join(card(d, f'{d["stem"]}.html', f' · {d["read_min"]} 分钟') for d in items)
        b = (f'<div class="crumb"><a href="../index.html">全部</a> / {html.escape(label)}</div>'
             f'<h1>{html.escape(label)}</h1><div class="cards">{cards}</div>')
        (OUT / slug / 'index.html').write_text(
            page(label, b, 1, slug, desc=f"{label} · 前沿科技知识库（{len(items)} 篇）",
                 canonical=f'{SITE_URL}/{slug}/index.html'), encoding='utf-8')

    # ---- 文档页 ----
    for i, d in enumerate(enriched):
        prev_d = enriched[i - 1] if i > 0 else None
        next_d = enriched[i + 1] if i + 1 < len(enriched) else None

        def href(o):
            if o['domain_slug'] == d['domain_slug']:
                return f"{o['stem']}.html"
            return f"../{o['domain_slug']}/{o['stem']}.html"

        pager = '<div class="pager">'
        pager += f'<a href="{href(prev_d)}">← {html.escape(prev_d["title"])}</a>' if prev_d else '<span></span>'
        pager += f'<a style="text-align:right" href="{href(next_d)}">{html.escape(next_d["title"])} →</a>' if next_d else ''
        pager += '</div>'

        toc_html = ''
        if len(d['toc']) >= 2:
            lis = ''.join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for _l, t, a in d['toc'])
            toc_html = f'<details class="toc" open><summary>本页目录（{len(d["toc"])} 节）</summary><ol>{lis}</ol></details>'

        chips = ''.join(f'<a class="chip" href="../tags.html#{slugify(t)}">{html.escape(t)}</a>'
                        for t in d['tags'])
        chips_html = f'<div class="chips">{chips}</div>' if d['tags'] else ''

        rel_html = ''
        if d['related']:
            rcards = ''.join(
                f'<a class="card" href="{("" if s == d["domain_slug"] else "../" + s + "/")}{st}.html">'
                f'<div class="t">{html.escape(t)}</div><div class="d">相关度 {round(sc, 3)}</div></a>'
                for t, s, st, sc in d['related'])
            rel_html = (f'<div class="rel"><h2>相关文档</h2><div class="cards">{rcards}</div></div>')

        b = (f'<div class="crumb"><a href="../index.html">全部</a> / '
             f'<a href="index.html">{html.escape(d["domain"])}</a> / {html.escape(d["title"])}</div>'
             f'<h1>{html.escape(d["title"])}</h1>'
             f'<div class="meta">{d["updated"]} · {html.escape(d["domain"])} · '
             f'{d["read_min"]} 分钟 · {len(d["refs"])} 条来源</div>'
             f'{chips_html}{toc_html}{d["body"]}{rel_html}{pager}')
        (OUT / d['domain_slug'] / f'{d["stem"]}.html').write_text(
            page(d['title'], b, 1, d['domain_slug'], desc=d['summary'],
                 canonical=f"{SITE_URL}/{d['url']}"), encoding='utf-8')

    # ---- 标签页 ----
    tags_sorted = sorted(tag_map.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    lookup = {d['url']: d for d in enriched}
    blocks = []
    for t, urls in tags_sorted:
        cards = ''
        for u in urls:
            d = lookup.get(u)
            if d:
                cards += card(d, u if d['domain_slug'] == '#' else u, f" · {d['read_min']} 分钟")
        blocks.append(f'<h2 id="{slugify(t)}">{html.escape(t)}（{len(urls)}）</h2>'
                      f'<div class="cards">{cards}</div>')
    tb = (f'<div class="crumb"><a href="index.html">全部</a> / 标签</div>'
          f'<h1>标签索引</h1><p class="meta">共 {len(tag_map)} 个标签，按文档数排序。'
          f'标签由标题概念与正文高频术语自动抽取（零依赖）。</p>' + '\n'.join(blocks))
    (OUT / 'tags.html').write_text(
        page('标签索引', tb, 0, None, desc='前沿科技知识库标签索引',
             canonical=f'{SITE_URL}/tags.html'), encoding='utf-8')

    # ---- RSS ----
    items = sorted(enriched, key=lambda d: d['updated'], reverse=True)[:30]
    rss = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0"><channel>',
           '<title>前沿科技知识库</title>',
           f'<link>{SITE_URL}/</link>',
           '<description>覆盖九大领域的前沿科技专题文档，逐条附来源链接</description>',
           '<language>zh-CN</language>',
           f'<lastBuildDate>{date.today().strftime("%a, %d %b %Y 00:00:00 +0000")}</lastBuildDate>']
    for d in items:
        rss.append('<item>')
        rss.append(f'<title>{html.escape(d["title"])}</title>')
        rss.append(f'<link>{SITE_URL}/{d["url"]}</link>')
        rss.append(f'<guid>{SITE_URL}/{d["url"]}</guid>')
        rss.append(f'<description>{html.escape(d["summary"])}</description>')
        if d['updated']:
            rss.append(f'<pubDate>{d["updated"]} 00:00:00 +0000</pubDate>')
        rss.append('</item>')
    rss.append('</channel></rss>')
    (OUT / 'feed.xml').write_text('\n'.join(rss), encoding='utf-8')

    # ---- sitemap / robots ----
    urls = ['<url><loc>%s/index.html</loc></url>' % SITE_URL,
            '<url><loc>%s/tags.html</loc></url>' % SITE_URL]
    urls += [f'<url><loc>{SITE_URL}/{s}/index.html</loc></url>' for s, _ in DOMAINS if by_domain.get(s)]
    for d in enriched:
        last = f'<lastmod>{d["updated"]}</lastmod>' if d['updated'] else ''
        urls.append(f'<url><loc>{SITE_URL}/{d["url"]}</loc>{last}</url>')
    (OUT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(urls) + '\n</urlset>\n', encoding='utf-8')
    (OUT / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n', encoding='utf-8')

    (OUT / '.nojekyll').write_text('', encoding='utf-8')
    print(f'构建完成：{len(enriched)} 篇文档 → {OUT}')
    print(f'  检索索引 {len(postings)} 词 / docs.json / graph.json / tags.json / feed.xml')
    return len(enriched)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='只校验能否构建，不写文件')
    args = ap.parse_args()
    build()
