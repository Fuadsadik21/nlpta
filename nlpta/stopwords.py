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
    return [token for token in tokens if token not in stopwords]