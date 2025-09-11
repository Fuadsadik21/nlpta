import re

def tokenize(text: str) -> list[str]:
    """
    Tokenize Amharic text into words.
    Uses regex to split on whitespace and punctuation.
    """
    # Remove punctuation first (if not already done)
    # This ensures we don't split on punctuation marks
    cleaned = re.sub(r'[።፣፤፥፦፧፨፠!?\"\'\(\)\[\]\{\}<>]', '', text)
    
    # Split on whitespace and return non-empty tokens
    tokens = [token.strip() for token in cleaned.split() if token.strip()]
    
    return tokens