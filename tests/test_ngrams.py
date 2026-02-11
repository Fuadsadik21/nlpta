from nlpta.ngrams import generate_ngrams


def test_generate_ngrams_from_tokens():
    assert generate_ngrams(["a", "b", "c"], n=2) == [("a", "b"), ("b", "c")]


def test_generate_ngrams_from_text():
    assert generate_ngrams("a b c", n=3) == [("a", "b", "c")]
