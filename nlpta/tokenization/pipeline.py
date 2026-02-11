"""
Tokenization pipeline for NLPTA.

This module composes sentence segmentation and word tokenization into
sentence-level token lists.
"""

from typing import List

from .sentences import segment_sentences
from .words import tokenize_words


def tokenize(text: str) -> List[List[str]]:
    """
    Tokenize text into sentences, then tokenize each sentence into words.
    """
    if not text:
        return []

    sentences = segment_sentences(text)
    return [tokenize_words(sentence) for sentence in sentences]


__all__ = ["tokenize"]
