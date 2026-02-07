import re

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
    text = remove_punctuation(text)
    text = clean_text(text)
    return text
def normalize_whitespace(text: str) -> str:
    """Normalize whitespace by replacing multiple spaces with a single space and trimming."""
    return re.sub(r'\s+', ' ', text).strip()
