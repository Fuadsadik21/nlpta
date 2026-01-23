import re

def tokenize_words(text: str) -> list[str]:
    """
    Tokenizes normalized Amharic text into words and punctuation marks.
    
    Parameters:
    text (str): The normalized Amharic text to tokenize.
    
    Returns:
    list[str]: An ordered list of tokens.
    """
    # Define the pattern to match Amharic punctuation marks
    punctuation_pattern = r'[:፠፡፣፤፦፧፨።]'
    
    # Split the text by whitespace while preserving punctuation marks
    tokens = re.split(r'(\s+)', text)
    
    # Filter out empty tokens that may result from multiple spaces
    tokens = [token for token in tokens if token.strip()]
    
    # Further split tokens by punctuation marks
    result = []
    for token in tokens:
        if re.search(punctuation_pattern, token):
            # Split the token by punctuation marks and add to result
            result.extend(re.split(f'({punctuation_pattern})', token))
        else:
            result.append(token)
    
    # Filter out any remaining empty tokens
    result = [token for token in result if token.strip()]
    
    return result