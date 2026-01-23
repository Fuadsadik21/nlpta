import re

def normalize_numerals(text: str) -> str:
    """
    Handles numerals by preserving Ethiopic and Arabic digits as-is, 
    while removing numeric noise such as thousands separators.
    
    This ensures that '3,000' or '3፣000' becomes '3000', facilitating 
    consistent tokenization in later stages.
    """
    if not text or not isinstance(text, str):
        return text

    # Remove commas (Western or Amharic) sitting between Arabic digits.
    # Pattern: Digit -> separator ( , or ፣ ) -> Digit
    # Replace with: Digit -> Digit (no separator)
    text = re.sub(r'(\d)[,፣](\d)', r'\1\2', text)

    return text