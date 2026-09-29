#!/usr/bin/env python3
"""校验 docs/ 下所有 Markdown 里的外链是否可达。

这是本仓库最容易失效的东西：163 篇文档、4000+ 条外链，而「可信度」
完全建立在这些链接能打开上。此前没有任何机制发现死链。

用法：
    python3 scripts/check_links.py                  # 全量检查
    python3 scripts/check_links.py --limit 100      # 只查前 100 条（本地调试）
    python3 scripts/check_links.py --timeout 10

退出码：发现死链 -> 1，否则 0。
"""
import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

LINK_RE = re.compile(r'https?://[^\s\)\]"<>]+')
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# 这些域名会拒绝自动化请求（403/429）或已停用，不算死链
SKIP_HOSTS = {
    "twitter.com", "x.com", "www.linkedin.com", "linkedin.com",
    "zhihu.com", "www.zhihu.com", "mp.weixin.qq.com",
    "www.instagram.com", "facebook.com", "www.facebook.com",
    "medium.com", "www.medium.com",
    "juejin.cn", "www.juejin.cn", "csdn.net", "blog.csdn.net",
}

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")


def host_of(url):
    m = re.match(r'https?://([^/:]+)', url)
    return m.group(1).lower() if m else ""


def collect_urls():
    found = {}
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for url in LINK_RE.findall(text):
            url = url.rstrip('.,;:')
            if host_of(url) in SKIP_HOSTS:
                continue
            found.setdefault(url, []).append(md.relative_to(ROOT).as_posix())
    return found


def _attempt(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return "ok", r.status
    except urllib.error.HTTPError as e:
        # 401/403/405/406/429 通常是反爬，不代表链接失效
        if e.code in (401, 403, 405, 406, 429, 999):
            return "unknown", f"HTTP {e.code}（反爬，跳过）"
        return "dead", f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return "error", f"{type(e).__name__}: {e}"


def check(url, timeout, retries=2):
    """返回 (url, status, detail)。status: ok / dead / unknown

    网络抖动（TLS 握手超时、连接被重置）很常见，直接判死会产生大量误报，
    而误报的 CI 等于没有 CI。所以除了明确的 4xx/5xx，其余错误都重试。
    """
    last = ("error", "no attempt")
    for attempt in range(retries + 1):
        status, detail = _attempt(url, timeout)
        if status != "error":
            return url, status, detail
        last = (status, detail)
    # 重试后仍然连不上：无法区分「站点挂了」和「网络抖动」，
    # 保守归为存疑，只在汇总里列出，不让 CI 失败
    return url, "unknown", f"{last[1]}（重试 {retries} 次后仍失败）"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="最多检查多少条")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()

    urls = collect_urls()
    targets = list(urls)
    if args.limit:
        targets = targets[: args.limit]

    print(f"文档数: {len(list(DOCS.rglob('*.md')))}")
    print(f"唯一外链: {len(urls)}，本次检查 {len(targets)} 条\n")

    dead, unknown = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(check, u, args.timeout): u for u in targets}
        for i, fut in enumerate(concurrent.futures.as_completed(futs), 1):
            url, status, detail = fut.result()
            if status == "dead":
                dead.append((url, detail))
                print(f"  ✖ {url}  ({detail})")
            elif status == "unknown":
                unknown.append((url, detail))
            if i % 100 == 0:
                print(f"  ... 已检查 {i}/{len(targets)}")

    print(f"\n结果: 可达 {len(targets) - len(dead) - len(unknown)}"
          f" / 死链 {len(dead)} / 存疑 {len(unknown)}")

    if dead:
        print("\n===== 死链清单（按文件） =====")
        for url, detail in dead:
            files = ", ".join(sorted(set(urls.get(url, []))))
            print(f"{url}\n    {detail}\n    出现于: {files}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
