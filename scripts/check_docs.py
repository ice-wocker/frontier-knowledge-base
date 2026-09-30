#!/usr/bin/env python3
"""知识库内容质量守门：结构、来源、元数据的一致性校验。

为什么需要它：这个库的价值全部建立在「每篇都结构统一、每条事实都能回溯」
上。而人写 163 篇（还会继续加）必然漂移——漏了「概述」、参考来源只剩两条、
标题重复、日期格式不统一。这类问题不影响构建，所以永远不会有人发现，
直到读者点进来觉得「这库不太行」。

`check_links.py` 管的是「外面的链接还活着吗」，本脚本管「里面写的东西还成立吗」。

用法：
    python3 scripts/check_docs.py            # 校验
    python3 scripts/check_docs.py --strict   # 把 warning 也当失败（PR 用）

退出码：有 error -> 1。
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import kb

# 每篇必须覆盖的「语义槽位」及其可接受的命名变体。
# 为什么用变体而不是固定标题：库里本来就存在「核心脉络与关键里程碑」
# 「核心概念与关键条款」这类更贴切场景的写法，硬性统一反而逼人降质。
# 校验的是「有没有讲到」，不是「标题叫什么」。
REQUIRED = {
    "概述":       ["概述", "简介", "是什么"],
    "最新进展":   ["最新进展", "进展", "现状"],
    # 「核心/关键」开头的章节都算讲到了技术/概念本体
    "核心技术":   ["核心", "关键", "原理"],
    "趋势与争议": ["趋势与争议", "争议", "趋势", "挑战"],
    "参考来源":   ["参考来源", "参考资料", "来源"],
}
# 建议覆盖（缺了只警告）
RECOMMENDED = {
    "代表性项目": ["代表性项目", "代表性", "代表产品", "主要项目", "典型"],
    "关键数据":   ["关键数据", "评测结果", "数据与"],
}

MIN_REFS = 5           # 参考来源少于这个数，可信度存疑
MAX_TITLE_LEN = 60     # 标题过长在卡片/搜索结果里会被截断
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="warning 也视为失败")
    args = ap.parse_args()

    docs = kb.load_docs()
    errors: list[str] = []
    warnings: list[str] = []

    def err(doc, msg):
        errors.append(f"{doc['path']}: {msg}")

    def warn(doc, msg):
        warnings.append(f"{doc['path']}: {msg}")

    # 1. 必备章节（按语义槽位 + 命名变体判断）
    for d in docs:
        secs = d["sections"]
        for slot, variants in REQUIRED.items():
            if not any(v in s for s in secs for v in variants):
                err(d, f"缺少内容槽位「{slot}」（可接受的标题：{'、'.join(variants)}）")
        for slot, variants in RECOMMENDED.items():
            if not any(v in s for s in secs for v in variants):
                warn(d, f"缺少建议槽位「{slot}」")

    # 2. 元信息行（最后更新 / 领域）
    for d in docs:
        if not d["updated"]:
            err(d, "缺少「最后更新：YYYY-MM-DD」")
        elif not DATE_RE.match(d["updated"]):
            err(d, f"日期格式不合法：{d['updated']}")
        if not d["field"]:
            warn(d, "缺少「领域：」描述")

    # 3. 参考来源数量
    for d in docs:
        n = len(kb.extract_refs(d["text"]))
        if n < MIN_REFS:
            err(d, f"参考来源仅 {n} 条（下限 {MIN_REFS}）")

    # 4. 标题：重复 / 过长
    titles = Counter(d["title"] for d in docs)
    for d in docs:
        if titles[d["title"]] > 1:
            err(d, f"标题重复：{d['title']}")
        if len(d["title"]) > MAX_TITLE_LEN:
            warn(d, f"标题过长（{len(d['title'])} 字符）：{d['title']}")

    # 5. 正文太短（可能是占位/半成品）
    for d in docs:
        body = kb.body_of(d["text"])
        if len(body) < 1500:
            warn(d, f"正文偏短（{len(body)} 字符）")

    # 7. 更新日期不应晚于今天（未来日期多半是手误）
    from datetime import date
    today = date.today().isoformat()
    for d in docs:
        if d["updated"] and d["updated"] > today:
            err(d, f"更新日期在未来：{d['updated']}")

    # 汇总
    print(f"文档数: {len(docs)}")
    print(f"领域数: {len({d['domain_slug'] for d in docs})}")
    print(f"来源链接(唯一): {len({u for d in docs for u in kb.extract_refs(d['text'])})}")
    print()

    if warnings:
        print(f"===== 警告 {len(warnings)} 条 =====")
        for w in warnings[:60]:
            print(f"  ⚠ {w}")
        if len(warnings) > 60:
            print(f"  ... 另有 {len(warnings) - 60} 条")
        print()

    if errors:
        print(f"===== 错误 {len(errors)} 条 =====")
        for e in errors:
            print(f"  ✖ {e}")
        return 1

    print("✅ 内容校验通过")
    if args.strict and warnings:
        print("✖ --strict 模式下警告视为失败")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
