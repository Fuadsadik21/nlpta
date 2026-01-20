from nlpta.preprocessing import tokenize, normalize_whitespace

def test_tokenize_returns_list():
    tokens = tokenize("አማርኛ ጽሑፍ")
    assert isinstance(tokens, list)

def test_normalize_whitespace_returns_string():
    text = normalize_whitespace("አማርኛ ጽሑፍ")
    assert isinstance(text, str)
