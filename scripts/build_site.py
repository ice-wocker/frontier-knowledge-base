#!/usr/bin/env python3
"""把 docs/ 下的 Markdown 渲染成一套静态站点（GitHub Pages）。

为什么要站点：163 篇文档全在 docs/ 里躺着，发现成本极高——没有检索、
没有目录页、没有「上一篇/下一篇」。内容质量已经够了，缺的只是形式。

设计取舍：
- 零依赖：不引入 MkDocs / VitePress，只用标准库。构建产物是纯静态 HTML，
  克隆下来双击 index.html 就能看，也方便以后换任何托管。
- 不碰原文：Markdown 是唯一真相源，站点只是投影；改内容只改 docs/。
- 索引一次生成：搜索用预生成的 JSON + 浏览器端过滤，不要后端。
"""
import argparse
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "site"

DOMAINS = [
    ("ai",        "人工智能（AI）"),
    ("hardware",  "硬件与半导体"),
    ("software",  "软件工程"),
    ("data",      "数据工程与数据平台"),
    ("security",  "网络安全"),
    ("science",   "基础科学前沿"),
    ("emerging",  "新兴科技"),
    ("industry",  "产业与政策"),
    ("society",   "社会与数字权利"),
]
DOMAIN_ORDER = {slug: i for i, (slug, _) in enumerate(DOMAINS)}
DOMAIN_LABEL = dict(DOMAINS)

TITLE_RE = re.compile(r'^#\s+(.+?)\s*$', re.M)
META_RE = re.compile(r'^>\s*最后更新：(\d{4}-\d{2}-\d{2})\s*｜\s*领域：([^｜]+)｜.*$', re.M)
SUMMARY_RE = re.compile(r'^##\s+概述\s*$', re.M)


# ---------- Markdown 渲染（只覆盖本仓库实际用到的子集） ----------

def esc(s):
    return html.escape(s, quote=False)


def inline(text):
    """行内元素：先转义，再处理 code / 粗体 / 链接，顺序不能反。"""
    text = esc(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # [文字](url)
    def link(m):
        label, url = m.group(1), m.group(2)
        ext = url.startswith('http')
        attrs = ' target="_blank" rel="noopener noreferrer"' if ext else ''
        return f'<a href="{url}"{attrs}>{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, text)
    return text


def render_markdown(md, doc_slug):
    """渲染正文。返回 HTML 字符串。"""
    lines = md.split('\n')
    out = []
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
                # H1 由模板负责，正文里跳过（避免重复）
                i += 1
                continue
            anchor = re.sub(r'[^\w\u4e00-\u9fff]+', '-', text).strip('-').lower()
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
    return '\n'.join(out)


# ---------- 元数据 ----------

def load_docs():
    items = []
    for slug, label in DOMAINS:
        d = DOCS / slug
        if not d.is_dir():
            continue
        for md in sorted(d.rglob('*.md')):
            text = md.read_text(encoding='utf-8')
            tm = TITLE_RE.search(text)
            title = tm.group(1).strip() if tm else md.stem
            mm = META_RE.search(text)
            updated = mm.group(1) if mm else ''
            domain = mm.group(2).strip() if mm else label
            items.append({
                'slug': slug,
                'domain': label,
                'domain_slug': slug,
                'title': title,
                'updated': updated,
                'path': md.relative_to(ROOT).as_posix(),
                'file': md,
                'text': text,
                'body': render_markdown(text, md.stem),
            })
    return items


# ---------- 模板 ----------

CSS = """
:root{--bg:#0d1117;--panel:#161b22;--border:#30363d;--fg:#e6edf3;--muted:#8b949e;
--accent:#58a6ff;--accent2:#7ee787;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header.top{position:sticky;top:0;background:rgba(13,17,23,.92);backdrop-filter:blur(8px);
border-bottom:1px solid var(--border);z-index:10}
.wrap{max-width:900px;margin:0 auto;padding:0 20px}
header.top .wrap{display:flex;align-items:center;gap:14px;height:56px}
header.top .brand{font-weight:600;white-space:nowrap}
header.top .brand em{color:var(--accent2);font-style:normal}
nav.domains{display:flex;gap:10px;overflow-x:auto;padding:12px 0;font-size:14px;
border-bottom:1px solid var(--border);scrollbar-width:thin}
nav.domains a{color:var(--muted);white-space:nowrap;padding:2px 8px;border-radius:6px}
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
footer{border-top:1px solid var(--border);color:var(--muted);font-size:.85rem;padding:22px 0 40px}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:3em;
padding-top:1.4em;border-top:1px solid var(--border);font-size:.9rem}
.pager a{max-width:48%}
@media(max-width:600px){h1{font-size:1.4rem}.wrap{padding:0 16px}}
"""

SEARCH_JS = """
(function(){
  var box=document.getElementById('q'), out=document.getElementById('results');
  if(!box) return;
  var data=null, timer=null;
  fetch('search.json').then(function(r){return r.json()}).then(function(j){data=j;});
  function render(kw){
    if(!data) return;
    kw=kw.trim().toLowerCase();
    if(!kw){out.innerHTML='';return;}
    var terms=kw.split(/\\s+/).filter(Boolean), hits=[];
    for(var i=0;i<data.length;i++){
      var d=data[i], hay=(d.title+' '+d.summary+' '+d.text).toLowerCase();
      var score=0, ok=true;
      for(var t=0;t<terms.length;t++){
        var idx=hay.indexOf(terms[t]);
        if(idx<0){ok=false;break;}
        score+=(d.title.toLowerCase().indexOf(terms[t])>=0)?50:1;
      }
      if(ok) hits.push([score,d]);
    }
    hits.sort(function(a,b){return b[0]-a[0]});
    hits=hits.slice(0,40);
    if(!hits.length){out.innerHTML='<p class="meta">没有匹配的文档。</p>';return;}
    out.innerHTML=hits.map(function(h){
      var d=h[1], s=d.summary||'';
      for(var t=0;t<terms.length;t++){
        var re=new RegExp('('+terms[t].replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&')+')','ig');
        s=s.replace(re,'<mark>$1</mark>');
      }
      return '<a class="hit" href="'+d.url+'"><div>'+d.title+'</div><div class="d">'+d.domain+(d.updated?' · '+d.updated:'')+'</div><div class="d">'+s+'</div></a>';
    }).join('');
  }
  box.addEventListener('input',function(){
    clearTimeout(timer); timer=setTimeout(function(){render(box.value)},120);
  });
})();
"""


def page(title, body, depth, active_slug=None, search=False):
    prefix = '../' * depth
    nav = ''.join(
        f'<a class="{"active" if s == active_slug else ""}" href="{prefix}{"index.html" if s == "ai" and depth == 0 else s + "/index.html"}">{html.escape(l)}</a>'
        for s, l in DOMAINS
    )
    nav = f'<a class="{"active" if active_slug == "all" else ""}" href="{prefix}index.html">全部</a>' + nav
    search_html = ''
    if search:
        search_html = '<input id="q" class="searchbox" type="search" placeholder="搜索 163 篇文档（标题 / 概要 / 正文）…" autocomplete="off"><div id="results"></div>'
    depth_script = ''
    if search:
        depth_script = f'<script>{SEARCH_JS}</script>'
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="前沿科技知识库 · {html.escape(title)}">
<meta name="color-scheme" content="dark light">
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
<header class="top"><div class="wrap"><span class="brand">🧊 <em>前沿科技</em>知识库</span></div>
<nav class="domains"><div class="wrap">{nav}</div></nav></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
内容基于公开网络资料整理，逐条附来源链接；不对来源准确性作担保，请以官方一手信息为准。<br>
<a href="https://github.com/ice-wocker/frontier-knowledge-base">在 GitHub 上查看源仓库</a>
</div></footer>
{depth_script}
</body>
</html>"""


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    docs = load_docs()
    (OUT / 'style.css').write_text(CSS, encoding='utf-8')

    # 搜索索引
    search = []
    for d in docs:
        plain = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', d['text'])
        plain = re.sub(r'[#>|*`]', ' ', plain)
        plain = re.sub(r'\s+', ' ', plain).strip()
        search.append({
            'title': d['title'],
            'domain': d['domain'],
            'updated': d['updated'],
            'summary': (plain[:180] + '…') if len(plain) > 180 else plain,
            'text': plain[:6000],
            'url': f"{d['domain_slug']}/{d['file'].stem}.html",
        })
    (OUT / 'search.json').write_text(json.dumps(search, ensure_ascii=False), encoding='utf-8')

    # 首页
    by_domain = {}
    for d in docs:
        by_domain.setdefault(d['domain_slug'], []).append(d)
    sections = []
    for slug, label in DOMAINS:
        items = by_domain.get(slug, [])
        if not items:
            continue
        cards = ''.join(
            f'<a class="card" href="{slug}/{d["file"].stem}.html">'
            f'<div class="t">{html.escape(d["title"])}</div>'
            f'<div class="d">{d["updated"]}</div></a>' for d in items
        )
        sections.append(
            f'<h2 id="{slug}">{html.escape(label)}（{len(items)} 篇）</h2>'
            f'<div class="cards">{cards}</div>'
        )
    body = f"""<div class="hero">
<h1>前沿科技知识库</h1>
<p>覆盖 AI、硬件半导体、软件工程、数据工程、网络安全、基础科学、新兴科技、产业与社会。
内容基于公开网络资料整理，关键事实就地标注来源，每篇文末附完整链接清单，可逐条回溯。</p>
</div>
<div class="stats">
<div><b>{len(docs)}</b>篇文档</div>
<div><b>{len(set(d['domain_slug'] for d in docs))}</b>个领域</div>
<div><b>0</b>个第三方依赖</div>
</div>
<input id="q" class="searchbox" type="search" placeholder="搜索 {len(docs)} 篇文档（标题 / 概要 / 正文）…" autocomplete="off">
<div id="results"></div>
""" + '\n'.join(sections)
    (OUT / 'index.html').write_text(page('前沿科技知识库', body, 0, 'all', search=True), encoding='utf-8')

    # 各领域页
    for slug, label in DOMAINS:
        items = by_domain.get(slug, [])
        if not items:
            continue
        ddir = OUT / slug
        ddir.mkdir(exist_ok=True)
        cards = ''.join(
            f'<a class="card" href="{d["file"].stem}.html">'
            f'<div class="t">{html.escape(d["title"])}</div>'
            f'<div class="d">{d["updated"]}</div></a>' for d in items
        )
        b = f'<div class="crumb"><a href="../index.html">全部</a> / {html.escape(label)}</div>' \
            f'<h1>{html.escape(label)}</h1><div class="cards">{cards}</div>'
        (ddir / 'index.html').write_text(page(label, b, 1, slug), encoding='utf-8')

    # 每篇文档
    seq = {d['file']: i for i, d in enumerate(docs)}
    for d in docs:
        ddir = OUT / d['domain_slug']
        i = seq[d['file']]
        prev_doc = docs[i - 1] if i > 0 else None
        next_doc = docs[i + 1] if i + 1 < len(docs) else None
        pager = ['<div class="pager">']
        if prev_doc:
            pager.append(f'<a href="{prev_doc["file"].stem}.html">← {html.escape(prev_doc["title"])}</a>')
        else:
            pager.append('<span></span>')
        if next_doc:
            pager.append(f'<a style="text-align:right" href="{next_doc["file"].stem}.html">{html.escape(next_doc["title"])} →</a>')
        pager.append('</div>')
        b = (f'<div class="crumb"><a href="../index.html">全部</a> / '
             f'<a href="index.html">{html.escape(d["domain"])}</a></div>'
             f'<h1>{html.escape(d["title"])}</h1>'
             f'<div class="meta">{d["updated"]} · {html.escape(d["domain"])}</div>'
             f'{d["body"]}{"".join(pager)}')
        (ddir / f'{d["file"].stem}.html').write_text(page(d['title'], b, 1, d['domain_slug']), encoding='utf-8')

    # .nojekyll 让 GitHub Pages 原样发布（下划线开头文件/目录）
    (OUT / '.nojekyll').write_text('', encoding='utf-8')
    print(f'构建完成：{len(docs)} 篇文档 → {OUT}')
    return len(docs)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='只校验能否构建，不写文件')
    args = ap.parse_args()
    build()
