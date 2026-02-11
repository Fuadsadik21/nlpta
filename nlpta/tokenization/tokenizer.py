"""
Canonical tokenization API for `nlpta.tokenization`.
"""

from ..preprocessing.tokenization import tokenize as _preprocess_tokenize


def tokenize(text: str) -> list[str]:
    """
    Tokenize text into whitespace-delimited word tokens with punctuation removed.
    """
    return _preprocess_tokenize(text)


__all__ = ["tokenize"]
