#!/usr/bin/env python3
"""从 docs/ 下的文档自动生成 INDEX.md。

README 里的目录是手写的，163 篇文档全靠人肉维护 —— 加一篇就得改一次 README，
迟早对不上（数量、链接、标题都会漂）。这个脚本以文件系统为唯一真相源。

用法：
    python3 scripts/gen_index.py           # 写入 INDEX.md
    python3 scripts/gen_index.py --check   # 只校验 INDEX.md 是否最新（CI 用）
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "INDEX.md"

# 领域目录 -> 中文名（顺序即 INDEX 中的展示顺序）
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

TITLE_RE = re.compile(r'^#\s+(.+?)\s*$', re.M)
UPDATED_RE = re.compile(r'最后更新：(\d{4}-\d{2}-\d{2})')
SUMMARY_RE = re.compile(r'^##\s+概述\s*$', re.M)


def first_sentence(text, limit=90):
    """取概述段的第一句作为摘要。"""
    m = SUMMARY_RE.search(text)
    body = text[m.end():] if m else text
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('>') or line.startswith('|'):
            continue
        # 去掉 markdown 链接，只留文字
        line = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', line)
        line = line.lstrip('-*• ').strip()
        if not line:
            continue
        # 按中文句号/问号/叹号或英文句点切第一句
        parts = re.split(r'(?<=[。！？])|(?<=\.)\s', line)
        s = parts[0].strip() if parts else line
        if len(s) > limit:
            s = s[:limit].rstrip() + '…'
        return s
    return ""


def collect():
    rows = {}
    for folder, label in DOMAINS:
        d = DOCS / folder
        if not d.is_dir():
            continue
        items = []
        for md in sorted(d.rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            tm = TITLE_RE.search(text)
            title = tm.group(1).strip() if tm else md.stem
            um = UPDATED_RE.search(text)
            items.append({
                "title": title,
                "path": md.relative_to(ROOT).as_posix(),
                "updated": um.group(1) if um else "",
                "summary": first_sentence(text),
            })
        rows[label] = items
    return rows


def render(rows):
    total = sum(len(v) for v in rows.values())
    lines = [
        "# 索引",
        "",
        f"> 由 `scripts/gen_index.py` 自动生成，共 **{total}** 篇文档。",
        "> 请勿手工编辑本文件——新增或改动文档后重新运行脚本即可。",
        "",
        "## 按领域",
        "",
        "| 领域 | 篇数 |",
        "| --- | ---: |",
    ]
    for label, items in rows.items():
        anchor = label.replace("（", "").replace("）", "").replace(" ", "-").lower()
        lines.append(f"| [{label}](#{anchor}) | {len(items)} |")
    lines.append("")

    for label, items in rows.items():
        lines += [f'<a id="{label.replace("（", "").replace("）", "").replace(" ", "-").lower()}"></a>', "",
                  f"## {label}（{len(items)} 篇）", "",
                  "| 文档 | 最后更新 | 概要 |", "| --- | --- | --- |"]
        for it in items:
            title = it["title"].replace("|", "\\|")
            summary = it["summary"].replace("|", "\\|")
            lines.append(f"| [{title}]({it['path']}) | {it['updated']} | {summary} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="校验 INDEX.md 是否为最新")
    args = ap.parse_args()

    content = render(collect())

    if args.check:
        if not OUT.exists():
            print("✖ INDEX.md 不存在，请运行 python3 scripts/gen_index.py")
            return 1
        if OUT.read_text(encoding="utf-8") != content:
            print("✖ INDEX.md 已过期，请运行 python3 scripts/gen_index.py 并提交结果")
            return 1
        print("✅ INDEX.md 是最新的")
        return 0

    OUT.write_text(content, encoding="utf-8")
    total = content.count("](docs/")
    print(f"✅ 已生成 {OUT.relative_to(ROOT)}（{total} 篇文档）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
