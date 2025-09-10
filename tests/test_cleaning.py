from nlpta import clean_text, normalize_whitespace, remove_punctuation

def test_clean_text():
    input_text = "  ሰላም አለም!   እንዴት ነህ?  "
    expected = "ሰላም አለም እንዴት ነህ"
    assert clean_text(input_text) == expected

def test_normalize_whitespace():
    text = "  አስመልክቶች    ይገኛል   "
    assert normalize_whitespace(text) == "አስመልክቶች ይገኛል"

def test_remove_punctuation():
    text = "እባኮት ፦ እናየሁ"
    assert remove_punctuation(text) == "እባኮት  እናየሁ"