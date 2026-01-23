"""
Amharic punctuation normalization.

This module removes non-linguistic symbols, preserves Amharic-specific
punctuation marks, and canonicalizes common ASCII punctuation into
their Amharic equivalents.
"""

import re

# Canonical Amharic punctuation marks to preserve
AMHARIC_PUNCTUATION = "፡።፣፤፦፧፨፠"

# Mapping from ASCII punctuation to Amharic equivalents
PUNCTUATION_MAP = {
    ".": "።",
    ",": "፣",
    ";": "፤",
    ":": "፦",
    "?": "፧",
}

# Regex pattern for non-linguistic symbols to remove
NON_LINGUISTIC_PATTERN = re.compile(r"[!@#$%^&*\(\)\[\]\{\}\"'<>/…]")

def normalize_punctuation(text: str) -> str:
    """
    Normalize punctuation in Amharic text.

    Steps:
    1. Convert common ASCII punctuation to canonical Amharic forms.
    2. Remove non-linguistic symbols.
    3. Preserve only valid Amharic punctuation marks.

    Parameters
    ----------
    text : str
        Raw input text.

    Returns
    -------
    str
        Text with normalized Amharic punctuation.
    """
    if not text:
        return text

    # Step 1: Canonicalize ASCII punctuation
    for ascii_punct, amharic_punct in PUNCTUATION_MAP.items():
        text = text.replace(ascii_punct, amharic_punct)

    # Step 2: Remove non-linguistic symbols
    text = NON_LINGUISTIC_PATTERN.sub("", text)

    # Step 3: Remove any remaining punctuation not Amharic
    text = re.sub(
        rf"[^\w\s{AMHARIC_PUNCTUATION}]",
        "",
        text,
        flags=re.UNICODE
    )

    return text
