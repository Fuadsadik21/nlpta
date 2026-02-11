import os

def load_stopwords(path=None):
    """
    Load stopwords from a file.

    Args:
        path (str | None): Optional path to the stopwords file.
            Defaults to data/stopwords.txt.

    Returns:
        set[str]: A set of stopwords.
    """
    if path is None:
        path = os.path.join("data", "stopwords.txt")

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

def remove_stopwords(tokens, stopwords=None):
    """
    Remove stopwords from a list of tokens.

    Args:
        tokens (list[str]): The list of tokens.
        stopwords (set[str] | None): The set of stopwords.
            If None, default stopwords are loaded from disk.

    Returns:
        list[str]: The filtered list of tokens.
    """
    if stopwords is None:
        stopwords = load_stopwords()

    return [token for token in tokens if token not in stopwords]
