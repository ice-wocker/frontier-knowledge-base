#!/usr/bin/env python3
"""站点产物自检：在没有浏览器的前提下，抓住最容易静默出错的问题。

为什么需要它：站点构建成功 ≠ 站点能用。下面这些错都曾经真实发生过，
而且构建阶段一片绿：

- `search.json` 被换成 `search-index.json` + `search/*.json` 之后，
  前端仍在请求旧文件 → 搜索框永远没结果，但页面看起来完全正常。
- 图标 / og 图 / manifest 写进了 <head>，产物里却没有这个文件 → 全是 404。
- 换域名时只改了 canonical，sitemap 和 og:url 还指向旧域。
- 领域导航指向不存在的目录。

这个脚本把「HTML 引用的每个站内文件都存在」当作硬约束来查，
外加结构、数量、地址一致性三类检查。

用法：
    python3 scripts/check_site.py          # 构建后运行（需要 site/ 存在）
    python3 scripts/check_site.py --build  # 先构建再检查
"""
import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# 站点对外地址的唯一真相源在 build_site.py 里
SITE_URL = None

ATTR_RE = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.I)
HEAD_ASSET_RE = re.compile(r'<(?:link|script|img)[^>]+(?:href|src)\s*=\s*"([^"]+)"', re.I)


def load_site_url():
    text = (ROOT / "scripts" / "build_site.py").read_text(encoding="utf-8")
    m = re.search(r'^SITE_URL\s*=\s*["\']([^"\']+)["\']', text, re.M)
    return m.group(1).rstrip("/") if m else None


def local_target(page: Path, ref: str):
    """把页面里的引用解析成磁盘路径；站外链接返回 None。"""
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
        return None
    ref = ref.split("#", 1)[0].split("?", 1)[0]
    if not ref:
        return None
    return (page.parent / unquote(ref)).resolve()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true", help="先重新构建站点")
    args = ap.parse_args()

    if args.build:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], check=True)

    if not (SITE / "index.html").exists():
        print("site/ 不存在，先运行 python3 scripts/build_site.py")
        return 1

    site_url = load_site_url()
    errors, warnings = [], []

    # ---- 1. 必需产物 ----
    required = ["index.html", "style.css", "search-index.json", "sitemap.xml",
                "robots.txt", "site.webmanifest", "favicon.svg",
                "apple-touch-icon.png", "og.svg", "feed.xml", ".nojekyll"]
    for f in required:
        if not (SITE / f).exists():
            errors.append(f"缺少产物 {f}")
    if not (SITE / "search").is_dir():
        errors.append("缺少 search/ 分片目录")

    # ---- 2. 页面里的站内引用必须都存在 ----
    pages = sorted(SITE.rglob("*.html"))
    missing = {}
    for page in pages:
        body = page.read_text(encoding="utf-8")
        # 去掉内联脚本，避免把 JS 里拼出来的路径当中引用
        stripped = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        for ref in ATTR_RE.findall(stripped):
            target = local_target(page, ref)
            if target is None:
                continue
            if not target.exists():
                missing.setdefault(ref, set()).add(page.relative_to(SITE).as_posix())
    for ref, where in sorted(missing.items()):
        errors.append(f"站内引用不存在：{ref}（出现于 {', '.join(sorted(where))[:120]}）")

    # ---- 3. head 里的资源必须存在，且 canonical / og:url 一致 ----
    for page in pages:
        body = page.read_text(encoding="utf-8")
        for ref in HEAD_ASSET_RE.findall(re.sub(r"<script>.*?</script>", "", body, flags=re.S)):
            if ref.startswith(("http", "//", "data:")):
                continue
            if not (page.parent / unquote(ref.split("?")[0])).resolve().exists():
                errors.append(f"{page.relative_to(SITE)} 的 head 引用了不存在的 {ref}")
        if not re.search(r'<meta charset="utf-8">', body, re.I):
            errors.append(f"{page.relative_to(SITE)} 缺 <meta charset>")
        if 'rel="canonical"' not in body:
            errors.append(f"{page.relative_to(SITE)} 缺 canonical")
        if "viewport" not in body:
            errors.append(f"{page.relative_to(SITE)} 缺 viewport")

    if site_url:
        idx = (SITE / "index.html").read_text(encoding="utf-8")
        canon = re.search(r'rel="canonical" href="([^"]+)"', idx)
        ok_canon = {f"{site_url}/", f"{site_url}/index.html"}
        if not canon or canon.group(1) not in ok_canon:
            errors.append(f"首页 canonical 应为 {site_url}/，实际 {canon.group(1) if canon else '缺失'}")
        sm = (SITE / "sitemap.xml").read_text(encoding="utf-8")
        locs = re.findall(r"<loc>([^<]+)</loc>", sm)
        bad = [u for u in locs if not u.startswith(site_url)]
        if bad:
            errors.append(f"sitemap 里有 {len(bad)} 条不是 SITE_URL 开头，例如 {bad[0]}")
        # 每篇文档都必须出现在 sitemap 里
        base_path = urlparse(site_url).path.strip("/")
        loc_paths = set()
        for u in locs:
            path = urlparse(u).path.lstrip("/")
            if base_path and path.startswith(base_path + "/"):
                path = path[len(base_path) + 1:]
            loc_paths.add(path)
        absent = [p.relative_to(SITE).as_posix() for p in pages
                  if p.name != "index.html"
                  and p.relative_to(SITE).as_posix() not in loc_paths]
        if absent:
            errors.append(f"sitemap 漏了 {len(absent)} 个页面，例如 {absent[0]}")
        feed = (SITE / "feed.xml").read_text(encoding="utf-8")
        if "<item>" not in feed:
            errors.append("feed.xml 里没有任何 item")

    # ---- 4. 搜索链路完整性：这也是「构建成功但搜索没结果」的根因 ----
    if (SITE / "search-index.json").exists():
        try:
            index = json.loads((SITE / "search-index.json").read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"search-index.json 不是合法 JSON：{e}")
            index = None
        if index:
            for key in ("docs", "buckets", "meta"):
                if key not in index:
                    errors.append(f"search-index.json 缺字段 {key}")
            # 分片必须都存在
            for b in index.get("buckets", []):
                if not (SITE / "search" / f"{b}.json").exists():
                    errors.append(f"索引声明了分片 {b}，但 search/{b}.json 不存在")
            # 文档条目必须齐全，且每个 url 都指向真实页面
            n_docs = len(index.get("docs", []))
            md_count = len(list((ROOT / "docs").rglob("*.md")))
            if n_docs != md_count:
                errors.append(f"索引里 {n_docs} 篇，docs/ 下有 {md_count} 篇")
            for d in index.get("docs", [])[:1000]:
                if not (SITE / d["url"]).exists():
                    errors.append(f"索引指向不存在的页面：{d['url']}")
                    break
            # 抽样验证：随机取几个词，必须能查到文档
            shards = {}
            for b in index.get("buckets", []):
                f = SITE / "search" / f"{b}.json"
                if f.exists():
                    shards.update(json.loads(f.read_text(encoding="utf-8")))
            samples = ["智能体", "安全", "模型", "数据"]
            for s in samples:
                if not any(s in term for term in shards):
                    warnings.append(f"索引里找不到词「{s}」——分词可能失效")

    # ---- 5. 索引体积（它决定首屏和搜索延迟，回退会很痛） ----
    if (SITE / "search-index.json").exists():
        total = sum(f.stat().st_size for f in (SITE / "search").glob("*.json"))
        total += (SITE / "search-index.json").stat().st_size
        print(f"检索索引合计：{total / 1024:.0f} KB（{len(list((SITE / 'search').glob('*.json')))} 个分片）")
        if total > 3 * 1024 * 1024:
            warnings.append(f"检索索引涨到 {total / 1024 / 1024:.1f} MB，检查是否又开始整段搬运正文")

    print(f"页面数：{len(pages)}")
    print(f"文档数：{len(list((ROOT / 'docs').rglob('*.md')))}")
    for w in warnings:
        print(f"  提示：{w}")
    if errors:
        print("\n发现问题：")
        for e in errors:
            print(f"  ✖ {e}")
        return 1
    print("\n全部通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
