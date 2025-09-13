import os

def load_stopwords():
    """Load curated Amharic stopwords from data/stopwords.txt."""
    filepath = os.path.join("data", "stopwords.txt")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            "Stopwords file not found. Please create data/stopwords.txt"
        )
    
    stopwords = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                stopwords.add(line)
    
    return stopwords

def remove_stopwords(tokens, stopwords=None):
    """Remove stopwords from a list of tokens."""
    if stopwords is None:
        stopwords = load_stopwords()
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