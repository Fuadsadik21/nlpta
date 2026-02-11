from nlpta.features import bag_of_words, tfidf_vectorize


def test_bag_of_words_from_namespace():
    assert bag_of_words("a b a") == {"a": 2, "b": 1}


def test_tfidf_vectorize_builds_expected_shape():
    vocab, matrix = tfidf_vectorize(["a a b", "b c"])
    assert vocab == ["a", "b", "c"]
    assert len(matrix) == 2
    assert len(matrix[0]) == 3
