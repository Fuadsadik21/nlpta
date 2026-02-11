from .sentence_splitter import split_sentences

# Backward-compatible alias.
segment_sentences = split_sentences

__all__ = ["split_sentences", "segment_sentences"]
