#!/usr/bin/env python3
"""知识库的公共引擎：解析 Markdown、分词、倒排索引、相似度。

为什么单独抽一个模块：`build_site.py` / `check_docs.py` / 未来的导出脚本
都要用同一套「文档是什么、词怎么切、谁和谁像」的定义。定义散在多处就会漂，
一处改了另一处不知道——这是知识库这种长期维护项目最容易烂的地方。

零依赖，只用标准库。
"""
from __future__ import annotations

import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# 领域目录 -> 中文名。顺序即展示顺序。
DOMAINS: list[tuple[str, str]] = [
    ("ai",       "人工智能（AI）"),
    ("hardware", "硬件与半导体"),
    ("software", "软件工程"),
    ("data",     "数据工程与数据平台"),
    ("security", "网络安全"),
    ("science",  "基础科学前沿"),
    ("emerging", "新兴科技"),
    ("industry", "产业与政策"),
    ("society",  "社会与数字权利"),
]
DOMAIN_LABEL = dict(DOMAINS)
DOMAIN_ORDER = {slug: i for i, (slug, _) in enumerate(DOMAINS)}

TITLE_RE = re.compile(r'^#\s+(.+?)\s*$', re.M)
UPDATED_RE = re.compile(r'最后更新：(\d{4}-\d{2}-\d{2})')
FIELD_RE = re.compile(r'领域：([^｜|\n]+)')
URL_RE = re.compile(r'https?://[^\s\)\]"<>]+')
H2_RE = re.compile(r'^##\s+(.+?)\s*$', re.M)

# 每篇文档应有的结构章节。用来做结构校验——缺章节是内容质量下降的最早信号。
REQUIRED_SECTIONS = ["概述", "最新进展", "核心技术与关键概念", "参考来源"]

STOPWORDS = {
    "the", "a", "an", "of", "to", "and", "or", "in", "on", "for", "with", "is", "are",
    "as", "by", "at", "from", "that", "this", "it", "be", "was", "were", "which", "how",
    "why", "what", "when", "has", "have", "had", "not", "but", "can", "will", "more",
    "的", "了", "是", "在", "和", "与", "及", "或", "对", "从", "到", "为", "以", "等",
    "这", "那", "一个", "一种", "我们", "他们", "可以", "以及", "通过", "进行", "基于",
    "使用", "提供", "实现", "包括", "比如", "例如", "其中", "目前", "已经", "成为",
}


# ---------- 解析 ----------

def doc_meta(md: Path) -> dict:
    """从单篇 Markdown 抽出结构化元数据。"""
    text = md.read_text(encoding="utf-8")
    rel = md.relative_to(ROOT).as_posix()
    slug = md.parent.name
    tm = TITLE_RE.search(text)
    title = tm.group(1).strip() if tm else md.stem
    um = UPDATED_RE.search(text)
    fm = FIELD_RE.search(text)
    secs = [s.strip() for s in H2_RE.findall(text)]
    return {
        "title": title,
        "path": rel,
        "file": md,
        "stem": md.stem,
        "domain_slug": slug,
        "domain": DOMAIN_LABEL.get(slug, slug),
        "updated": um.group(1) if um else "",
        "field": fm.group(1).strip() if fm else "",
        "sections": secs,
        "text": text,
    }


def load_docs() -> list[dict]:
    """按领域顺序加载全部文档。"""
    items: list[dict] = []
    for slug, _label in DOMAINS:
        d = DOCS / slug
        if not d.is_dir():
            continue
        for md in sorted(d.rglob("*.md")):
            items.append(doc_meta(md))
    items.sort(key=lambda x: (DOMAIN_ORDER.get(x["domain_slug"], 99), x["title"]))
    return items


def body_of(text: str) -> str:
    """去掉标题行与元信息引用行，只留正文（用于分词/相似度）。"""
    lines = []
    for line in text.splitlines():
        if line.startswith("#"):
            continue
        if line.startswith(">") and "最后更新" in line:
            continue
        lines.append(line)
    return "\n".join(lines)


def body_no_refs(text: str) -> str:
    """正文去掉「参考来源」章节。引用的 URL 里全是域名和标题碎片，
    拿它们当标签/主题信号只会污染结果。"""
    return text.split("## 参考来源")[0] if "## 参考来源" in text else text


def extract_refs(text: str) -> list[str]:
    """参考来源章节里的链接（去重、保序）。"""
    sec = text.split("## 参考来源")[-1] if "## 参考来源" in text else ""
    seen, out = set(), []
    for u in URL_RE.findall(sec):
        u = u.rstrip('.,;:')
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


# ---------- 分词 ----------

_CJK = r'\u4e00-\u9fff'
_TOKEN_RE = re.compile(rf'[{_CJK}]+|[A-Za-z][A-Za-z0-9+#._-]*|\d+')


def tokenize(text: str) -> list[str]:
    """中英混合分词（零依赖）。

    - 英文/数字：按词切，统一小写，去掉 stopword
    - 中文：单字 + 相邻二字组合（bigram）。没有分词器时这是
      「召回」与「体积」之间最稳的折中：bigram 能表达「向量检索」
      这种复合概念，又不至于像 trigram 那样把索引撑爆。
    """
    text = text.lower()
    out: list[str] = []
    for m in _TOKEN_RE.finditer(text):
        tok = m.group(0)
        if re.match(rf'^[{_CJK}]+$', tok):
            if len(tok) == 1:
                out.append(tok)
            else:
                out.extend(tok[i:i + 2] for i in range(len(tok) - 1))
        elif tok.isdigit():
            out.append(tok)
        else:
            if len(tok) >= 2 and tok not in STOPWORDS:
                out.append(tok)
    return out


def terms_from_query(q: str) -> list[str]:
    """查询串 -> 检索词。与 tokenize 同规则，保证索引/查询一致。"""
    return tokenize(q)


# ---------- 倒排索引 ----------

def build_index(docs: list[dict], min_df: int = 2, max_df_ratio: float = 0.6) -> dict:
    """构建倒排索引 + 文档向量（用于打分与相似度）。

    结构：
        postings: {term: {doc_id: tf}}
        df: {term: 文档频率}
        dl: [每篇长度]
        idf: {term: 逆文档频率}

    两头都做裁剪：
    - df < min_df：只在 1 篇里出现的词。中文 bigram 会产生海量这种词
      （52K 个，占索引 2/3），而它们对多词查询毫无贡献（只命中一篇，
      排序也进不了前排）。实测 min_df=1 -> 2 检索质量零变化，体积腰斩。
    - df > 总数 * max_df_ratio：出现频率过高的词（如「模型」在 AI
      领域几乎每篇都有）区分度接近 0，留着只会撑大索引。
    """
    postings: dict[str, dict[int, int]] = {}
    dl: list[int] = []
    for i, d in enumerate(docs):
        toks = tokenize(body_of(d["text"]))
        dl.append(len(toks))
        tf: dict[str, int] = {}
        for t in toks:
            tf[t] = tf.get(t, 0) + 1
        for t, c in tf.items():
            postings.setdefault(t, {})[i] = c

    n = len(docs) or 1
    df = {t: len(p) for t, p in postings.items()}
    idf = {
        t: math.log(1 + (n - d + 0.5) / (d + 0.5))
        for t, d in df.items()
    }
    # 过滤超高频词（对体积贡献最大，对检索贡献最小）
    hi = max(min_df, 2)
    keep = {t for t, d in df.items() if hi <= d <= max(hi, n * max_df_ratio)}
    postings = {t: p for t, p in postings.items() if t in keep}
    idf = {t: v for t, v in idf.items() if t in keep}

    # 文档向量（tf-idf 归一化），用于余弦相似度
    vecs: list[dict[str, float]] = [{} for _ in docs]
    for t, p in postings.items():
        for i, c in p.items():
            vecs[i][t] = (1 + math.log(c)) * idf[t]
    for v in vecs:
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        for k in v:
            v[k] /= norm

    return {"postings": postings, "df": df, "dl": dl, "idf": idf,
            "vecs": vecs, "n": len(docs)}


def search(index: dict, docs: list[dict], query: str, limit: int = 40) -> list[tuple[int, float]]:
    """BM25 检索。返回 [(doc_id, score)]，降序。

    标题命中额外加权——搜「围棋」时，标题里就写着「围棋」的文档
    比正文顺带提一句的更该排前面。
    """
    terms = terms_from_query(query)
    if not terms:
        return []
    qtf: dict[str, int] = {}
    for t in terms:
        qtf[t] = qtf.get(t, 0) + 1

    scores: dict[int, float] = {}
    postings = index["postings"]
    idf = index["idf"]
    dl = index["dl"]
    avgdl = (sum(dl) / len(dl)) if dl else 1.0
    k1, b = 1.5, 0.75

    for t, qc in qtf.items():
        p = postings.get(t)
        if not p:
            continue
        w = idf.get(t, 0.0) * (1 + math.log(qc))
        for i, tf in p.items():
            dl_i = dl[i] if i < len(dl) else avgdl
            denom = tf + k1 * (1 - b + b * (dl_i / avgdl if avgdl else 1))
            scores[i] = scores.get(i, 0.0) + w * (tf * (k1 + 1)) / (denom or 1)

    # 标题加权
    for i in scores:
        tl = docs[i]["title"].lower()
        for t in qtf:
            if t in tl:
                scores[i] += 3.0 * idf.get(t, 0.0)

    return sorted(scores.items(), key=lambda kv: -kv[1])[:limit]


def related(docs: list[dict], index: dict, i: int, k: int = 4) -> list[tuple[int, float]]:
    """与第 i 篇最相似的 k 篇（余弦相似度）。

    用文档向量做两两比较。163 篇的距离是 163² ≈ 2.6 万次点积，
    构建期跑一次完全无压力，换来每篇页面上的「相关文档」。
    """
    vi = index["vecs"][i]
    out = []
    for j, vj in enumerate(index["vecs"]):
        if j == i:
            continue
        if docs[j]["domain_slug"] != docs[i]["domain_slug"]:
            continue  # 只在同领域内推荐：跨领域相似度天然偏低，噪声大
        s = sum(w * vj.get(t, 0.0) for t, w in vi.items())
        if s > 0:
            out.append((j, s))
    out.sort(key=lambda kv: -kv[1])
    if len(out) < k:  # 同领域不够就看全库，保证每篇都有推荐
        seen = {j for j, _ in out}
        for j, vj in enumerate(index["vecs"]):
            if j == i or j in seen:
                continue
            s = sum(w * vj.get(t, 0.0) for t, w in vi.items())
            if s > 0:
                out.append((j, s))
        out.sort(key=lambda kv: -kv[1])
    return out[:k]


# 标签里的「词」应当是有意义的术语，而不是域名/文件路径/年份这类东西。
# 这些词在任何技术文档里都高频出现，当标签没有区分度
_LOW_VALUE = {
    "papers", "paper", "howto", "general", "national", "artificial", "images",
    "image", "data", "model", "models", "tools", "tool", "guide", "overview",
    "introduction", "report", "reports", "news", "blog", "article", "index",
    "html", "pdf", "http", "https",
}

_BAD_TAG = re.compile(
    r'(^\d+$)'
    r'|(^https?$)'
    r'|(^www$)'
    r'|(\.(com|org|net|io|ai|cn|co|dev|gov|edu|pdf|html)$)'
    r'|(^[a-z]{1,2}$)'          # 单双字母（da / ai 之外的碎片）
    r'|(^\d{4}$)'              # 纯年份
)


def tags_for(doc: dict, index: dict, docs: list[dict], top: int = 8) -> list[str]:
    """从正文里提取「标签」（术语）。

    刻意不用 NLP 抽关键词——那需要模型，会破坏零依赖。这里用最朴素但
    可解释的做法：取该文档 tf-idf 最高的英文术语 + 标题里的中文概念词。

    关键在过滤：tf-idf 高分里混着大量域名（openaccess.thecvf.com）、
    年份（cvpr2026）、单字母碎片（da）——它们只是「本文出现过且别处不常见」，
    当标签毫无意义。所以要求：纯字母数字/连字符、长度 >= 3、不是域名、
    不是纯数字，且**至少出现在正文 3 次**（偶发提及不算主题）。
    """
    from collections import Counter
    v = index["vecs"][docs.index(doc)]
    # 统计英文词频（只在正文里数，标题另算）
    freq = Counter(t for t in tokenize(body_of(body_no_refs(doc["text"])))
                   if re.fullmatch(r'[a-z][a-z0-9+#._-]{2,}', t))
    ranked = sorted(v.items(), key=lambda kv: -kv[1])
    out: list[str] = []
    seen_stems: set[str] = set()
    for term, _w in ranked:
        if len(out) >= top:
            break
        if not re.fullmatch(r'[a-z][a-z0-9+#._-]{2,}', term):
            continue
        if _BAD_TAG.search(term):
            continue
        if ('thecvf' in term) or ('arxiv' == term) or ('openaccess' in term):
            continue
        if term.endswith(('.com', '.org', '.net', '.io', '.cn', '.dev', '.pdf')):
            continue
        if freq.get(term, 0) < 3:
            continue
        # URL slug 特征：超长、含多个连字符、或带点号（域名）
        if len(term) > 18 or term.count('-') >= 2 or '.' in term:
            continue
        stem = term[:-1] if term.endswith('s') and len(term) > 4 else term
        if stem in seen_stems or term in _LOW_VALUE:
            continue
        if term not in out:
            out.append(term)
            seen_stems.add(stem)
    # 标题里的中文词组（按分隔符切）
    for part in re.split(r'[（(）)、，,·—\-–/｜|]+', doc["title"]):
        part = part.strip()
        if 2 <= len(part) <= 12 and re.search(rf'[{_CJK}]', part) and part not in out:
            out.append(part)
        if len(out) >= top:
            break
    return out[:top]


def reading_minutes(text: str) -> int:
    """粗略阅读时长：中文按 350 字/分，英文按 200 词/分。"""
    n = len(re.findall(rf'[{_CJK}]', text))
    m = len(re.findall(r'\b[A-Za-z]{2,}\b', text))
    return max(1, round(n / 350 + m / 200))
