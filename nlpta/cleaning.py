import re

def normalize_whitespace(text: str) -> str:
    """Normalize multiple whitespaces to single space."""
    return re.sub(r'\s+', ' ', text).strip()

def remove_punctuation(text: str) -> str:
    """Remove common Amharic punctuation."""
    punctuation = "።፣፤፥፦፧፨፠"
    for p in punctuation:
        text = text.replace(p, "")
    return text

def clean_text(text: str) -> str:
    """Clean Amharic text."""
    text = normalize_whitespace(text)
    text = remove_punctuation(text)
    return text