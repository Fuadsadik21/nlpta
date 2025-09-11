from nlpta.cleaning import clean_text, normalize_whitespace, remove_punctuation

def test_clean_text():
    """Normalize all whitespace to single space and strip ends."""
    assert clean_text("  ሰላም አለም!   እንዴት ነህ?  ") == "ሰላም አለም እንዴት ነህ"

def test_normalize_whitespace():
        """Remove common Amharic and English punctuation."""
        assert normalize_whitespace("  ሰላም   አለም  ") == "ሰላም አለም"

def test_remove_punctuation():
        """Clean Amharic text by normalizing whitespace and removing punctuation."""
        assert remove_punctuation("ሰላም አለም! እንዴት ነህ?") == "ሰላም አለም እንዴት ነህ"