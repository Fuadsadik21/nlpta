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
    assert "ኢትዮጵያ" in filtered
    assert "ሕዝብ" in filtered
    assert "ዓመት" in filtered