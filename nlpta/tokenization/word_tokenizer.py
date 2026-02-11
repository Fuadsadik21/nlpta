"""
Word-level tokenization helpers.
"""

from .tokenizer import tokenize


def word_tokenize(text: str) -> list[str]:
    """
    Alias for the package-level `tokenize` function.
    """
    return tokenize(text)


__all__ = ["word_tokenize"]
