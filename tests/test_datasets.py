from nlpta.datasets import load_sample_corpus

def test_load_sample_corpus():
    corpus = load_sample_corpus()
    assert len(corpus) > 0
    assert isinstance(corpus[0], str)
    assert len(corpus[0]) > 10