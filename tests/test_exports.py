import nlpta
from nlpta.tokenization import tokenize


def test_top_level_exports_exist():
    assert callable(nlpta.load_stopwords)
    assert callable(nlpta.load_embeddings)
    assert callable(nlpta.generate_ngrams)


def test_tokenize_export():
    assert tokenize("a b c") == ["a", "b", "c"]
