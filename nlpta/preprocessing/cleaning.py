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
    text = clean_text(text)
    return text
CHAR_VARIANT_MAP = {
    "ሐ": "ሀ",
    "ሑ": "ሁ",
    "ሒ": "ሂ",
    "ሓ": "ሃ",
    "ሔ": "ሄ",
    "ሕ": "ህ",
    "ሖ": "ሆ",
    "ኀ": "ሀ",
    "ኁ": "ሁ",
    "ኂ": "ሂ",
    "ኃ": "ሀ",
    "ኄ": "ሄ",
    "ኅ": "ህ",
    "ኆ": "ሆ",
    "ሓ": "ሀ",
    "ሃ": "ሀ",
    "ኻ": "ሀ",

    "ሠ": "ሰ",
    "ሱ": "ሡ",
    "ሲ": "ሢ",
    "ሳ": "ሣ",
    "ሴ": "ሤ",
    "ስ": "ሥ",
    "ሶ": "ሦ",

    "ጸ": "ፀ",
    

    "ዐ": "አ",
    "ዓ": "አ",
    "ዔ": "ኤ",
    "ዕ": "እ",
    "ዖ": "ኦ",
    "ዓ": "አ",
    "ዑ": "ኡ",
    "ዒ": "ኢ",
    "ዓ": "አ",
    "ዔ": "ኤ",
    "ዕ": "እ",
    "ዖ": "ኦ",
}
def normalize_characters(text: str) -> str:
    for src, tgt in CHAR_VARIANT_MAP.items():
        text = text.replace(src, tgt)
    return text
