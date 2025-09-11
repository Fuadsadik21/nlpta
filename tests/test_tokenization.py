from nlpta.tokenization import tokenize

def test_tokenize():
    text = "ሰላም አለም! እንዴት ነህ?"
    expected = ["ሰላም", "አለም", "እንዴት", "ነህ"]
    assert tokenize(text) == expected