"""
Tokenization pipeline for NLPTA.

This module composes sentence segmentation and word tokenization
into a single, stable API for downstream use.

Assumes input text is already normalized (Phase 1).
"""

from typing import List

from .sentences import segment_sentences
from .words import tokenize_words


def tokenize(text: str) -> List[List[str]]:
    """
    Tokenize normalized Amharic text into sentences and word-level tokens.

    Parameters
    ----------
    text : str
        Normalized Amharic text.

    Returns
    -------
    List[List[str]]
        A list of sentences, where each sentence is a list of tokens.
    """
    if not text:
        return []

    sentences = segment_sentences(text)
    return [tokenize_words(sentence) for sentence in sentences]
text = "እኔ ትምህርት እማራለሁ። አንተ ምን ታደርጋለህ፧"
print(tokenize(text))