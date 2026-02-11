"""
TF-IDF feature extraction for small to medium corpora.
"""

import math
from typing import Dict, List, Optional, Sequence, Tuple, Union

from .bow import _normalize_tokens, build_vocabulary

Document = Union[str, Sequence[str]]


def tfidf_vectorize(
    corpus: Sequence[Document],
    vocabulary: Optional[Sequence[str]] = None,
    lowercase: bool = False,
    smooth_idf: bool = True
) -> Tuple[List[str], List[List[float]]]:
    """
    Vectorize documents using TF-IDF.

    Args:
        corpus: Sequence of documents as raw strings or token lists.
        vocabulary: Optional vocabulary order/filter.
        lowercase: Whether to lowercase tokens before vectorization.
        smooth_idf: Apply sklearn-style IDF smoothing.

    Returns:
        tuple[list[str], list[list[float]]]:
            - ordered vocabulary
            - matrix with one row per document and one column per term
    """
    if not corpus:
        return [], []

    tokenized_docs = [_normalize_tokens(document, lowercase=lowercase) for document in corpus]

    if vocabulary is None:
        vocab = build_vocabulary(tokenized_docs, lowercase=False)
    else:
        seen = set()
        vocab = []
        for term in vocabulary:
            normalized_term = str(term).lower() if lowercase else str(term)
            if normalized_term in seen:
                continue
            seen.add(normalized_term)
            vocab.append(normalized_term)

    if not vocab:
        return [], [[0.0] * 0 for _ in tokenized_docs]

    # Count terms per document and document frequency per term.
    term_counts = []
    document_frequency = {term: 0 for term in vocab}
    for tokens in tokenized_docs:
        counts = {term: 0 for term in vocab}
        for token in tokens:
            if token in counts:
                counts[token] += 1
        term_counts.append(counts)
        for term in vocab:
            if counts[term] > 0:
                document_frequency[term] += 1

    num_docs = len(tokenized_docs)
    idf_scores = {}
    for term in vocab:
        df = document_frequency[term]
        if smooth_idf:
            idf_scores[term] = math.log((1 + num_docs) / (1 + df)) + 1.0
        elif df > 0:
            idf_scores[term] = math.log(num_docs / df) + 1.0
        else:
            idf_scores[term] = 0.0

    matrix = []
    for doc_index, tokens in enumerate(tokenized_docs):
        doc_length = len(tokens)
        row = []
        for term in vocab:
            tf = (term_counts[doc_index][term] / doc_length) if doc_length else 0.0
            row.append(tf * idf_scores[term])
        matrix.append(row)

    return vocab, matrix


def tfidf(
    corpus: Sequence[Document],
    vocabulary: Optional[Sequence[str]] = None,
    lowercase: bool = False,
    smooth_idf: bool = True
) -> List[Dict[str, float]]:
    """
    TF-IDF as a list of term-score dictionaries (one per document).
    """
    vocab, matrix = tfidf_vectorize(
        corpus=corpus,
        vocabulary=vocabulary,
        lowercase=lowercase,
        smooth_idf=smooth_idf
    )
    return [dict(zip(vocab, row)) for row in matrix]


__all__ = ["tfidf", "tfidf_vectorize"]
