"""
Compatibility exports for embedding utilities.
"""

from .models.embeddings import get_embedding, load_embeddings, load_word_embeddings

__all__ = ["load_embeddings", "load_word_embeddings", "get_embedding"]
