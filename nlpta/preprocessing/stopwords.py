import os

def load_stopwords(path):
    """
    Load stopwords from a file.

    Args:
        path (str): Path to the stopwords file.

    Returns:
        set[str]: A set of stopwords.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            "Stopwords file not found. Please create data/stopwords.txt"
        )
    
    stopwords = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                stopwords.add(line)
    
    return stopwords

def remove_stopwords(tokens, stopwords):
    """
    Remove stopwords from a list of tokens.

    Args:
        tokens (list[str]): The list of tokens.
        stopwords (set[str]): The set of stopwords.

    Returns:
        list[str]: The filtered list of tokens.
    """
    # Remove stopwords and also strip stopword prefixes from tokens
    filtered_tokens = []
    for token in tokens:
        # Check for any stopword as a prefix
        matched_prefix = None
        for sw in stopwords:
            if token.startswith(sw) and len(token) > len(sw):
                matched_prefix = sw
                break
        if matched_prefix:
            stripped = token[len(matched_prefix):]
            if stripped and stripped not in stopwords:
                filtered_tokens.append(stripped)
        elif token not in stopwords:
            filtered_tokens.append(token)
    return filtered_tokens