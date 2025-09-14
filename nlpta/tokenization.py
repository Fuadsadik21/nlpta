import re

def tokenize(text):
    """
    Tokenize the input text into a list of tokens.

    Args:
        text (str): The input text.

    Returns:
        list[str]: The list of tokens.
    """
    # Remove punctuation first
    cleaned = re.sub(r'[።፣፤፥፦፧፨፠!?\"\'\(\)\[\]\{\}<>]', '', text)
    # Split on whitespace and return non-empty tokens
    tokens = [token.strip() for token in cleaned.split() if token.strip()]
    return tokens