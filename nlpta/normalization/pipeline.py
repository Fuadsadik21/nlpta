from .characters import normalize_characters
from .punctuation import normalize_punctuation
from .whitespace import normalize_whitespace
from .numerals import normalize_numerals

def normalize(text: str) -> str:
    """
    The master normalization pipeline for Amharic text.
    
    Order of Operations:
    1. Character Variant Normalization (Structural consistency)
    2. Punctuation Normalization (Canonicalizes/removes symbols)
    3. Whitespace Normalization (Cleans spacing artifacts)
    4. Numeral Handling (Final cleaning of numeric noise)
    """
    if not text or not isinstance(text, str):
        return text

    # Step 1: Canonicalize orthographic variants (ሐ -> ሀ, etc.)
    text = normalize_characters(text)
    
    # Step 2: Handle punctuation mappings and symbol removal
    text = normalize_punctuation(text)
    
    # Step 3: Collapse whitespaces and trim
    text = normalize_whitespace(text)
    
    # Step 4: Clean numeric separators (3,000 -> 3000)
    text = normalize_numerals(text)

    return text