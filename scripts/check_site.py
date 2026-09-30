#!/usr/bin/env python3
"""站点产物自检：构建成功后，验证「站点真的能用」。

`build_site.py` 只能证明「渲染没报错」，证明不了「站点是对的」。这类静默故障
包括：站内链接指向不存在的页面、sitemap 里的 URL 打不开、检索索引里的
docId 越界（点进去 404）、canonical 声明了一个连不上的域名。

之前的版本只查「链接能不能打开」，挡不住上面这些。本脚本专接
「构建成功但站点坏掉」。

用法：
    python3 scripts/check_site.py                  # 校验已构建的 site/
    python3 scripts/check_site.py --build          # 先构建再校验
    python3 scripts/check_site.py --online         # 额外检查入口地址是否可达
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

HREF_RE = re.compile(r'(?:href|src)="([^"#?]+)(?:[#?][^"]*)?"')
# 内联 <script> 里会拼字符串（如 'href="'+d.u+'"'），不是真链接。
SCRIPT_RE = re.compile(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>',
                       re.S | re.I)


def fail(msg):
    print(f"  ✖ {msg}")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true", help="先运行构建")
    ap.add_argument("--online", action="store_true", help="检查线上入口是否可达")
    args = ap.parse_args()

    if args.build:
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")])
        if r.returncode != 0:
            return r.returncode

    if not SITE.is_dir():
        return fail("site/ 不存在，请先运行 scripts/build_site.py")

    errors = 0

    # 1. 站内链接：每个 href/src 都必须指向真实存在的文件
    print("检查站内链接…")
    missing = {}
    htmls = list(SITE.rglob("*.html"))
    for h in htmls:
        base = h.parent
        # 去掉内联脚本/样式，避免把 JS 拼接的字符串当成链接
        text = SCRIPT_RE.sub('', h.read_text(encoding="utf-8"))
        for href in HREF_RE.findall(text):
            if href.startswith(("http://", "https://", "mailto:", "data:", "javascript:")):
                continue
            target = (base / href).resolve()
            if not target.exists():
                missing.setdefault(href, set()).add(h.relative_to(SITE).as_posix())
    for href, srcs in sorted(missing.items())[:30]:
        errors += fail(f"站内链接失效 {href} ← {', '.join(sorted(srcs)[:3])}")
    if not missing:
        print(f"  ✓ {len(htmls)} 个页面，站内链接全部有效")

    # 2. 检索索引：docId 必须落在 docs 范围内
    print("检查检索索引…")
    try:
        idx = json.loads((SITE / "search-index.json").read_text(encoding="utf-8"))
        meta = json.loads((SITE / "docs.json").read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return fail(f"索引文件无法解析：{e}")
    n = meta["count"]
    if len(meta["docs"]) != n:
        errors += fail(f"docs.json count={n} 与 docs 数组长度 {len(meta['docs'])} 不符")
    oob = 0
    for term, flat in idx["p"].items():
        for i in range(0, len(flat), 2):
            if not (0 <= flat[i] < n):
                oob += 1
    if oob:
        errors += fail(f"检索索引有 {oob} 个越界 docId")
    else:
        print(f"  ✓ {len(idx['p'])} 个词，docId 全部在 [0,{n}) 内")

    # 3. 索引里指向的页面必须真实存在
    print("检查索引指向的页面…")
    bad = []
    for d in meta["docs"]:
        if not (SITE / d["u"]).exists():
            bad.append(d["u"])
    for u in bad[:20]:
        errors += fail(f"docs.json 指向不存在的页面 {u}")
    if not bad:
        print(f"  ✓ {n} 篇文档页面全部存在")

    # 4. sitemap / feed 的 URL 必须与 canonical 同源
    print("检查 sitemap / RSS / canonical 同源…")
    sm = (SITE / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>(.+?)</loc>", sm)
    hosts = {re.match(r"https?://[^/]+", u).group(0) for u in locs}
    if len(hosts) != 1:
        errors += fail(f"sitemap 出现多个主机：{hosts}")
    else:
        print(f"  ✓ sitemap {len(locs)} 条，主机 {hosts.pop()}")
    if not (SITE / "feed.xml").read_text(encoding="utf-8").count("<item>"):
        errors += fail("feed.xml 没有任何条目")

    # 5. 必需产物
    for f in ["index.html", "tags.html", "style.css", "search-index.json",
              "docs.json", "graph.json", "tags.json", "feed.xml",
              "sitemap.xml", "robots.txt", ".nojekyll"]:
        if not (SITE / f).exists():
            errors += fail(f"缺少产物 {f}")

    # 6. 线上入口可达（可选）
    if args.online and locs:
        entry = locs[0]
        print(f"检查入口 {entry} …")
        try:
            req = urllib.request.Request(entry, headers={"User-Agent": "kb-check"})
            with urllib.request.urlopen(req, timeout=15) as r:
                print(f"  ✓ HTTP {r.status}")
        except urllib.error.HTTPError as e:
            errors += fail(f"入口返回 HTTP {e.code}")
        except Exception as e:  # noqa: BLE001
            errors += fail(f"入口不可达：{e}")

    if errors:
        print(f"\n✖ 站点自检失败，{errors} 个问题")
        return 1
    print("\n✅ 站点自检通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
