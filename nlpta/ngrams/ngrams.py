"""
N-gram generation utilities.
"""

from typing import List, Sequence, Tuple, Union

TokenInput = Union[str, Sequence[str]]


def generate_ngrams(tokens_or_text: TokenInput, n: int = 2) -> List[Tuple[str, ...]]:
    """
    Generate token-level n-grams from text or tokens.

    Args:
        tokens_or_text: A whitespace-delimited string or a token sequence.
        n: N-gram size (must be positive).

    Returns:
        list[tuple[str, ...]]: Ordered n-gram tuples.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    if isinstance(tokens_or_text, str):
        tokens = [token for token in tokens_or_text.split() if token]
    else:
        tokens = [str(token).strip() for token in tokens_or_text if str(token).strip()]

    if len(tokens) < n:
        return []

    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def ngrams(tokens_or_text: TokenInput, n: int = 2) -> List[Tuple[str, ...]]:
    """
    Backward-compatible alias for `generate_ngrams`.
    """
    return generate_ngrams(tokens_or_text=tokens_or_text, n=n)


__all__ = ["generate_ngrams", "ngrams"]
