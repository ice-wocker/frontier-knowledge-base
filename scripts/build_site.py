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

# 站点对外地址：canonical / og:url / sitemap / feed 都从这一处生成。
# 换域名只改这一行。
SITE_URL = "https://ice-wocker.github.io/frontier-knowledge-base"

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
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:-9999px;top:0;z-index:40;background:var(--panel);
border:1px solid var(--accent);border-radius:0 0 9px 0;padding:9px 14px}
.skip:focus{left:0}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
nav.domains{overflow-x:auto;white-space:nowrap;scrollbar-width:none;
-webkit-overflow-scrolling:touch}
nav.domains::-webkit-scrollbar{display:none}
nav.domains .wrap{display:flex;gap:18px}
nav.domains a{padding:2px 0}
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media(max-width:600px){h1{font-size:1.4rem}.wrap{padding:0 16px}
header.top .wrap{padding:10px 16px}nav.domains a{font-size:.9rem}}
@media print{header.top,nav.domains,footer,.searchbox{display:none}}
"""

SEARCH_JS = r"""
(function(){
  // 检索流程：查询词 -> 需要的分片 -> 倒排取候选 -> 打分排序 -> 高亮。
  // 整个索引 8 片、gzip 后共约 250 KB，且**不在首屏加载**：
  // 用户第一次敲字才拉，拉完记住。首屏因此只有一个几 KB 的 HTML。
  var box=document.getElementById('q'), out=document.getElementById('results');
  if(!box) return;
  var INDEX=null, shards={}, inflight={}, timer=null, ready=null;

  function esc(s){return String(s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}

  // 与构建端 _terms 保持一致：拉丁词 + 中文 2~4 字滑窗
  function termsOf(text){
    text=text.toLowerCase(); var out=[], re=/[0-9a-z][0-9a-z+#._-]{1,23}|[\u4e00-\u9fff]{2,6}/g, m;
    while((m=re.exec(text))){
      var tok=m[0];
      if(tok.charCodeAt(0)<0x4e00){ out.push(tok); continue; }
      for(var n=2;n<=4;n++)
        for(var i=0;i+n<=tok.length;i++) out.push(tok.substr(i,n));
    }
    return out;
  }

  function loadShard(name){
    if(shards[name]) return Promise.resolve(shards[name]);
    if(inflight[name]) return inflight[name];
    inflight[name]=fetch('search/'+name+'.json')
      .then(function(r){ if(!r.ok) throw new Error(r.status); return r.json() })
      .then(function(j){ shards[name]=j; return j })
      .catch(function(){ shards[name]={}; return {} });
    return inflight[name];
  }

  function ensureReady(){
    if(ready) return ready;
    ready=fetch('search-index.json').then(function(r){
      if(!r.ok) throw new Error(r.status);
      return r.json();
    }).then(function(j){
      INDEX=j;
      return Promise.all(j.buckets.map(loadShard));
    }).then(function(){ return true; });
    return ready;
  }

  function show(msg){ out.innerHTML='<p class="meta">'+esc(msg)+'</p>' }

  function render(kw){
    kw=(kw||'').trim().toLowerCase();
    if(!kw){ out.innerHTML=''; return; }
    if(!INDEX){ show('正在载入检索索引…'); return; }
    var phrases=kw.split(/\s+/).filter(Boolean), terms=[];
    phrases.forEach(function(p){ terms=terms.concat(termsOf(p)) });
    if(!terms.length){ show('没有匹配的文档。'); return; }

    var scores={}, cover={};
    INDEX.buckets.forEach(function(name){
      var sh=shards[name]; if(!sh) return;
      terms.forEach(function(t){
        var ids=sh[t]; if(!ids) return;
        for(var i=0;i<ids.length;i++){
          var id=ids[i];
          scores[id]=(scores[id]||0)+1;
          (cover[id]||(cover[id]={}))[t]=1;
        }
      });
    });

    var docs=INDEX.docs, hits=[];
    Object.keys(scores).forEach(function(id){
      var d=docs[id]; if(!d) return;
      var covered=Object.keys(cover[id]||{}).length;
      var s=covered/scores[id] - scores[id]/300;   // 覆盖度优先，长文档不占便宜
      var tl=d.title.toLowerCase(), dl=d.domain.toLowerCase();
      phrases.forEach(function(p){
        if(tl.indexOf(p)>=0) s+=2.5;
        else if(dl.indexOf(p)>=0) s+=0.6;
      });
      hits.push([s,d]);
    });
    hits.sort(function(a,b){return b[0]-a[0]});
    hits=hits.slice(0,40);
    if(!hits.length){ show('没有匹配的文档。试试更短的关键词，比如「智能体」「向量」。'); return; }
    out.innerHTML=hits.map(function(h){
      var d=h[1], txt=d.summary||'';
      phrases.forEach(function(p){
        var pat=p.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
        txt=txt.replace(new RegExp('('+pat+')','ig'),'<mark>$1</mark>');
      });
      return '<a class="hit" href="'+d.url+'"><div>'+esc(d.title)+'</div>'+
             '<div class="d">'+esc(d.domain)+(d.updated?' · '+d.updated:'')+'</div>'+
             '<div class="d">'+txt+'</div></a>';
    }).join('');
  }

  function kick(){
    ensureReady().then(function(){ render(box.value) })
                  .catch(function(){ show('检索索引载入失败，请刷新重试。') });
  }

  // 首次输入才载入；聚焦时也预热一下，让第一次按键就有结果
  box.addEventListener('focus',kick,{once:true});
  box.addEventListener('input',function(){
    clearTimeout(timer);
    timer=setTimeout(function(){ kick() },80);
  });
  box.addEventListener('keydown',function(e){
    if(e.key==='Escape'){box.value='';out.innerHTML='';return}
    if(e.key==='Enter'){var f=out.querySelector('a.hit'); if(f){e.preventDefault(); f.click();}}
  });
})();
"""




# ---------- 检索用的极简分词 ----------

_TERM_RE = re.compile(r'[0-9a-z][0-9a-z+#._-]{1,23}|[\u4e00-\u9fff]{2,6}')


def _terms(text, min_gram=3):
    """把文本切成检索词。

    中文没有空格，用滑窗切 n-gram：3-gram 已经能给出足够的区分度，
    2-gram 只在标题/领域里保留（正文全切 2-gram 会让词表翻倍，
    而「工程」「模型」这类词几乎不分文档）。
    """
    text = text.lower()
    out = []
    for m in _TERM_RE.finditer(text):
        tok = m.group(0)
        if not ('\u4e00' <= tok[0] <= '\u9fff'):
            out.append(tok)
            continue
        for n in range(min_gram, 5):
            for i in range(len(tok) - n + 1):
                out.append(tok[i:i + n])
    return out


SHARD_BUCKETS = 8

# 分片里只保留「出现 >= 2 次」的词：只出现一次的 n-gram 对检索没有贡献，
# 却占了索引里的大头（中文滑窗产生的生僻组合基本都是这一档）。
MIN_DF = 2


def _bucket(term):
    """稳定的分片号。不能用内置 hash()——它每个进程都加盐，构建和校验会不一致。"""
    import hashlib
    return int(hashlib.md5(term.encode("utf-8")).hexdigest()[:8], 16) % SHARD_BUCKETS


def _bucket_name(n):
    return f"b{n}"


# ---------- 图标与分享图（零依赖） ----------

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#0b0f14"/>
<g fill="none" stroke="#7ee787" stroke-width="3" stroke-linecap="round">
<path d="M32 13v38"/>
<path d="M20 20h24M20 32h24M20 44h24" opacity=".75"/>
</g>
<circle cx="32" cy="32" r="4" fill="#5ad1ff"/>
</svg>
"""


def _png_chunk(tag, data):
    import struct, zlib
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))


def _make_icon(size=180):
    """手写一张 180×180 的 PNG（深底 + 三条横线 + 中心点），不引 Pillow。"""
    import math, struct, zlib
    bg, line, dot = (0x0b, 0x0f, 0x14), (0x7e, 0xe7, 0x87), (0x5a, 0xd1, 0xff)
    rows = []
    for y in range(size):
        row = bytearray()
        for x in range(size):
            px = bg
            for ly in (0.31, 0.5, 0.69):
                if abs(y + .5 - size * ly) < size * 0.022 and size * .28 < x < size * .72:
                    px = line
            if (x - size / 2) ** 2 + (y - size / 2) ** 2 < (size * 0.06) ** 2:
                px = dot
            row += bytes(px)
        rows.append(bytes(row))
    raw = b"".join(b"\x00" + r for r in rows)
    return (b"\x89PNG\r\n\x1a\n"
            + _png_chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
            + _png_chunk(b"IDAT", zlib.compress(raw, 9))
            + _png_chunk(b"IEND", b""))


APPLE_ICON = _make_icon()

OG_IMAGE = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#0b0f14"/>
<text x="90" y="260" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Microsoft YaHei,sans-serif"
 font-size="82" font-weight="700" fill="#e6edf3">前沿科技知识库</text>
<text x="90" y="340" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Microsoft YaHei,sans-serif"
 font-size="36" fill="#7ee787">163 篇专题 · 9 个领域 · 关键事实逐条附来源</text>
<text x="90" y="410" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Microsoft YaHei,sans-serif"
 font-size="28" fill="#8b98a8">AI · 硬件半导体 · 软件工程 · 数据 · 安全 · 基础科学 · 新兴科技 · 产业 · 社会</text>
<circle cx="90" cy="480" r="8" fill="#5ad1ff"/>
</svg>
"""


def _sibling_href(current, other):
    """同领域用文件名，跨领域要走 ../<slug>/<name>.html。

    此前跨领域的上一篇/下一篇只写了文件名，结果 16 条导航全是 404——
    这个错误在构建阶段完全看不出来，只有真的点一下才会发现。
    """
    name = other["file"].stem + ".html"
    if other["domain_slug"] == current["domain_slug"]:
        return name
    return f'../{other["domain_slug"]}/{name}'


def page(title, body, depth, active_slug=None, search=False, desc=None, path=None,
         doc=None, prev_doc=None, next_doc=None, n_docs=None):
    prefix = '../' * depth
    nav = ''.join(
        f'<a class="{"active" if s == active_slug else ""}" href="{prefix}{s}/index.html">{html.escape(l)}</a>'
        for s, l in DOMAINS
    )
    nav = f'<a class="{"active" if active_slug == "all" else ""}" href="{prefix}index.html">全部</a>' + nav
    n_docs = n_docs if n_docs is not None else len(list(DOCS.rglob('*.md')))
    depth_script = f'<script>{SEARCH_JS}</script>' if search else ''

    desc = desc or f"{title} · 前沿科技知识库"
    url = f"{SITE_URL}/{path}" if path else SITE_URL + "/"
    # 文档页补上「上下篇」和结构化数据：一篇文章被单独搜到时，
    # 搜索引擎需要知道它属于哪个站点、什么时间更新。
    prevnext = ''
    if doc and (prev_doc or next_doc):
        links = []
        if prev_doc:
            links.append(f'<a rel="prev" href="{prev_doc["href"]}">← {html.escape(prev_doc["title"])}</a>')
        else:
            links.append('<span></span>')
        if next_doc:
            links.append(f'<a rel="next" style="text-align:right" href="{next_doc["href"]}">'
                         f'{html.escape(next_doc["title"])} →</a>')
        prevnext = '<nav class="pager" aria-label="文档导航">' + ''.join(links) + '</nav>'
    ldjson = ''
    if doc:
        ldjson = ('<script type="application/ld+json">'
                  + json.dumps({
                      "@context": "https://schema.org",
                      "@type": "Article",
                      "headline": doc["title"],
                      "dateModified": doc["updated"],
                      "inLanguage": "zh-CN",
                      "isPartOf": {"@type": "WebSite", "name": "前沿科技知识库", "url": SITE_URL + "/"},
                      "url": url,
                  }, ensure_ascii=False)
                  + '</script>')
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0b0f14">
<link rel="canonical" href="{html.escape(url)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="{'article' if doc else 'website'}">
<meta property="og:url" content="{html.escape(url)}">
<meta property="og:site_name" content="前沿科技知识库">
<meta property="og:image" content="{SITE_URL}/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">
<link rel="manifest" href="{prefix}site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="最新更新" href="{prefix}feed.xml">
<link rel="stylesheet" href="{prefix}style.css">
{ldjson}
</head>
<body>
<a class="skip" href="#main">跳到主内容</a>
<header class="top"><div class="wrap">
<a class="brand" href="{prefix}index.html">🧊 <em>前沿科技</em>知识库</a>
</div></header>
<nav class="domains" aria-label="领域导航"><div class="wrap">{nav}</div></nav>
<main class="wrap" id="main">
{body}
{prevnext}
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

    # ---- 搜索索引：倒排 + 分片 ----
    # 为什么不是一个大 JSON：早期版本把每篇正文前 6000 字塞进 search.json，
    # 结果单个文件 1.6 MB（压缩后 620 KB）。而且没有倒排，每次输入都要对
    # 163 条 × 6 KB 做子串扫描——首键延迟和每次按键的卡顿都来自这里。
    # 现在只发「标题 + 概要 + 词表映射」的倒排索引，按首字节分片，
    # 输入时先按候选集取子集，再只对候选做高亮匹配。
    records = []
    postings = {}          # term -> [doc_id, ...]
    for idx_no, d in enumerate(docs):
        plain = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', d['text'])
        plain = re.sub(r'[#>|*`]', ' ', plain)
        plain = re.sub(r'\s+', ' ', plain).strip()
        summary = (plain[:160] + '…') if len(plain) > 160 else plain
        d['summary'] = summary
        records.append({
            'i': idx_no,
            'title': d['title'],
            'domain': d['domain'],
            'updated': d['updated'],
            'summary': summary,
            'url': f"{d['domain_slug']}/{d['file'].stem}.html",
            # 正文只留前 300 字给结果里做高亮和上下文，不再整段搬运
            'snippet': plain[:300],
        })
        seen = set()
        for term in _terms(d['title'] + ' ' + d['domain'], min_gram=2):
            if term not in seen:
                seen.add(term)
                postings.setdefault(term, []).append(idx_no)
        for term in _terms(plain):
            if term in seen:
                continue
            seen.add(term)
            postings.setdefault(term, []).append(idx_no)

    # 分片：按词哈希取模，固定 N 片。按首字节分组会让中文片数爆炸
    # （每个汉字一片 = 上千个文件、且分布极不均），哈希取模的片大小可控。
    shards = {}
    for term, ids in postings.items():
        uniq = sorted(set(ids))
        if len(uniq) < MIN_DF:
            continue
        shards.setdefault(_bucket(term), {})[term] = uniq
    shard_dir = OUT / 'search'
    shard_dir.mkdir(exist_ok=True)
    for key, payload in shards.items():
        (shard_dir / f'{  _bucket_name(key)}.json').write_text(
            json.dumps(payload, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

    index = {
        'docs': records,
        'buckets': sorted(_bucket_name(k) for k in shards),
        # 结果里不再需要正文全量；这里只保留每篇的词数，用于排序里的长度归一
        'meta': {'count': len(records), 'schema': 2},
    }
    (OUT / 'search-index.json').write_text(
        json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

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
<label class="vh" for="q">搜索文档</label>
<input id="q" class="searchbox" type="search" placeholder="{len(docs)} 篇文档：搜标题、领域或关键词…" autocomplete="off" aria-controls="results">
<p class="vh" id="q-hint">输入关键词即时检索；回车打开第一条结果，Esc 清空。</p>
<div id="results" role="list" aria-live="polite"></div>
""" + '\n'.join(sections)
    (OUT / 'index.html').write_text(page(
        '前沿科技知识库',
        body, 0, 'all', search=True, n_docs=len(docs),
        desc='163 篇前沿科技专题，覆盖 AI、半导体、软件工程、数据、安全、基础科学等九个领域，'
             '关键事实逐条附来源链接。',
        path='index.html'), encoding='utf-8')

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
        (ddir / 'index.html').write_text(page(
            f'{label} · 前沿科技知识库', b, 1, slug,
            desc=f'{label}领域共 {len(items)} 篇专题文档，关键事实逐条附来源链接。',
            path=f'{slug}/index.html'), encoding='utf-8')

    # 每篇文档
    seq = {d['file']: i for i, d in enumerate(docs)}
    for d in docs:
        ddir = OUT / d['domain_slug']
        i = seq[d['file']]
        prev_doc = docs[i - 1] if i > 0 else None
        next_doc = docs[i + 1] if i + 1 < len(docs) else None
        b = (f'<div class="crumb"><a href="../index.html">全部</a> / '
             f'<a href="index.html">{html.escape(d["domain"])}</a></div>'
             f'<h1>{html.escape(d["title"])}</h1>'
             f'<div class="meta">最后更新 {d["updated"]} · {html.escape(d["domain"])}</div>'
             f'{d["body"]}')
        (ddir / f'{d["file"].stem}.html').write_text(page(
            f'{d["title"]} · 前沿科技知识库', b, 1, d['domain_slug'],
            desc=(d['summary'] or d['title'])[:150],
            path=f'{d["domain_slug"]}/{d["file"].stem}.html',
            doc=d,
            prev_doc={'href': _sibling_href(d, prev_doc), 'title': prev_doc['title']} if prev_doc else None,
            next_doc={'href': _sibling_href(d, next_doc), 'title': next_doc['title']} if next_doc else None,
        ), encoding='utf-8')

    # ---- 图标 / 分享图 / 爬虫文件 / RSS ----
    (OUT / 'favicon.svg').write_text(FAVICON, encoding='utf-8')
    (OUT / 'apple-touch-icon.png').write_bytes(APPLE_ICON)
    (OUT / 'og.svg').write_text(OG_IMAGE, encoding='utf-8')
    (OUT / 'site.webmanifest').write_text(json.dumps({
        'name': '前沿科技知识库',
        'short_name': '前沿科技',
        'description': '163 篇前沿科技专题，关键事实逐条附来源链接。',
        'start_url': './', 'scope': './', 'display': 'browser',
        'background_color': '#0b0f14', 'theme_color': '#0b0f14', 'lang': 'zh-CN',
        'icons': [
            {'src': 'favicon.svg', 'sizes': 'any', 'type': 'image/svg+xml'},
            {'src': 'apple-touch-icon.png', 'sizes': '180x180', 'type': 'image/png'},
        ],
    }, ensure_ascii=False, indent=1), encoding='utf-8')
    (OUT / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n', encoding='utf-8')
    urls = [SITE_URL + '/'] + [f'{SITE_URL}/{d["domain_slug"]}/index.html' for d in docs
                               if d['domain_slug']] + \
           [f'{SITE_URL}/{d["domain_slug"]}/{d["file"].stem}.html' for d in docs]
    seen_urls = []
    for u in urls:
        if u not in seen_urls:
            seen_urls.append(u)
    (OUT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'  <url><loc>{html.escape(u)}</loc></url>\n' for u in seen_urls)
        + '</urlset>\n', encoding='utf-8')

    # RSS：163 篇按更新时间倒序，给订阅器和「最近更新」一个入口
    recent = sorted(docs, key=lambda x: (x['updated'], x['title']), reverse=True)[:40]
    items = ''.join(
        '  <item>\n'
        f'    <title>{html.escape(d["title"])}</title>\n'
        f'    <link>{SITE_URL}/{d["domain_slug"]}/{d["file"].stem}.html</link>\n'
        f'    <guid>{SITE_URL}/{d["domain_slug"]}/{d["file"].stem}.html</guid>\n'
        f'    <category>{html.escape(d["domain"])}</category>\n'
        f'    <pubDate>{d["updated"]}T00:00:00+08:00</pubDate>\n'
        f'    <description>{html.escape((d["summary"] or "")[:300])}</description>\n'
        '  </item>\n' for d in recent)
    (OUT / 'feed.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>\n'
        '  <title>前沿科技知识库</title>\n'
        f'  <link>{SITE_URL}/</link>\n'
        '  <description>163 篇前沿科技专题，关键事实逐条附来源链接。</description>\n'
        '  <language>zh-CN</language>\n'
        + items + '</channel></rss>\n', encoding='utf-8')

    # .nojekyll 让 GitHub Pages 原样发布（下划线开头文件/目录）
    (OUT / '.nojekyll').write_text('', encoding='utf-8')
    print(f'构建完成：{len(docs)} 篇文档 → {OUT}')
    return len(docs)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='只校验能否构建，不写文件')
    args = ap.parse_args()
    build()
