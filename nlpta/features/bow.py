"""
Bag-of-words helpers for lightweight feature extraction.
"""

from collections import Counter
from typing import Dict, List, Optional, Sequence, Union

Document = Union[str, Sequence[str]]


def _normalize_tokens(document: Document, lowercase: bool = False) -> List[str]:
    """
    Convert a raw text string or token sequence into cleaned tokens.
    """
    if isinstance(document, str):
        tokens = document.split()
    else:
        tokens = [str(token) for token in document]

    normalized = []
    for token in tokens:
        token = token.strip()
        if not token:
            continue
        if lowercase:
            token = token.lower()
        normalized.append(token)
    return normalized


def build_vocabulary(corpus: Sequence[Document], lowercase: bool = False) -> List[str]:
    """
    Build a sorted vocabulary from a corpus.
    """
    vocabulary = set()
    for document in corpus:
        vocabulary.update(_normalize_tokens(document, lowercase=lowercase))
    return sorted(vocabulary)


def bag_of_words(
    text: Document,
    vocabulary: Optional[Sequence[str]] = None,
    lowercase: bool = False
) -> Dict[str, int]:
    """
    Create a bag-of-words vector for a single document.

    Args:
        text: Raw string or sequence of tokens.
        vocabulary: Optional term order/filter. When provided, output contains
            only these terms (missing terms are set to 0).
        lowercase: Whether to lowercase tokens before counting.

    Returns:
        dict[str, int]: Mapping from term to count.
    """
    counts = Counter(_normalize_tokens(text, lowercase=lowercase))

    if vocabulary is None:
        return dict(counts)

    ordered_terms = []
    seen = set()
    for term in vocabulary:
        normalized_term = str(term).lower() if lowercase else str(term)
        if normalized_term in seen:
            continue
        seen.add(normalized_term)
        ordered_terms.append(normalized_term)

    return {term: counts.get(term, 0) for term in ordered_terms}


__all__ = ["bag_of_words", "build_vocabulary"]
