"""nlpta: Amharic NLP Toolkit package."""

from .cleaning import clean_text
from .datasets import load_sample_corpus
from .tokenization import tokenize
from .stopwords import load_stopwords, remove_stopwords
from .embeddings import load_embeddings

__all__ = [
    "clean_text",
    "load_sample_corpus",
    "tokenize",
    "load_stopwords",
    "remove_stopwords",
    "load_embeddings"
]