# Mapping dictionary as defined in Phase 1 specification
CANONICAL_MAP = {
    "ሐ": "ሀ",
    "ኀ": "ሀ",
    "ሓ": "ሀ",
    "ኻ": "ሀ",
    "ሃ": "ሀ",
    "ኅ": "ሀ",
    "ኃ": "ሀ",
    "ሠ": "ሰ",
    "ጸ": "ፀ",
    "ዐ": "አ",
    "ዓ": "አ",
}

# Pre-compute translation table for performance (single pass)
_TRANSLATION_TABLE = str.maketrans(CANONICAL_MAP)

def normalize_characters(text: str) -> str:
    """
    Reduces orthographic variation by mapping Amharic character variants 
    to a single canonical form.
    
    This helps in reducing vocabulary size and handling spelling variations 
    without altering the underlying semantics.
    """
    if not text or not isinstance(text, str):
        return text

    return text.translate(_TRANSLATION_TABLE)