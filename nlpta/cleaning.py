import re

def normalize_whitespace(text: str) -> str:
    """Normalize all whitespace to single space and strip ends."""
    return re.sub(r'\s+', ' ', text).strip()

def remove_punctuation(text: str) -> str:
    """Remove common Amharic and English punctuation."""
    punctuation = "።፣፤፥፦፧፨፠!?\"'()[]{}<>"
    for p in punctuation:
        text = text.replace(p, "")
    return text

def clean_text(text):
    """
    Clean the input text by removing unwanted characters, normalizing whitespace, or applying other preprocessing steps.

    Args:
        text (str): The input text to clean.

    Returns:
        str: The cleaned text.
    """
    text = normalize_whitespace(text)
    text = remove_punctuation(text)
    return text