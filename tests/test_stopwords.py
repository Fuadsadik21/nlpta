from nlpta import tokenize, remove_stopwords, load_stopwords

def test_remove_stopwords():
    stopwords = load_stopwords()
    assert len(stopwords) > 0, "Stopwords list is empty!"
    
    text = "በኢትዮጵያ ውስጥ የሚገኘው ሕዝብ በዓመት ይጨምራል"
    tokens = tokenize(text)
    filtered = remove_stopwords(tokens)
    
    # Should remove functional words
    assert "በ" not in filtered
    assert "ውስጥ" not in filtered
    
    # Should keep meaningful words
    assert "በኢትዮጵያ" in filtered
    assert "ሕዝብ" in filtered
    assert "በዓመት" in filtered

def test_remove_stopwords_empty_input():
    stopwords = load_stopwords()
    tokens = []
    filtered = remove_stopwords(tokens, stopwords)
    assert filtered == []

def test_remove_stopwords_all_stopwords():
    stopwords = load_stopwords()
    # Use only stopwords (pick first 3 from stopwords set)
    tokens = list(stopwords)[:3]
    filtered = remove_stopwords(tokens, stopwords)
    assert filtered == []

def test_remove_stopwords_no_stopwords():
    stopwords = load_stopwords()
    tokens = ["አማርኛ", "ቋንቋ", "ሙዚቃ"]
    filtered = remove_stopwords(tokens, stopwords)
    assert filtered == tokens

def test_remove_stopwords_mixed_case():
    stopwords = load_stopwords()
    # If stopwords are case-sensitive, this should not remove "በ"
    tokens = ["በ", "በኢትዮጵያ", "በ"]
    filtered = remove_stopwords(tokens, stopwords)
    assert all(token not in stopwords for token in filtered)