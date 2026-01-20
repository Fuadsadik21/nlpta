import os

def load_sample_corpus():
    """
    Load the sample Amharic corpus from the data directory.

    Returns:
        list[str]: A list of paragraphs from the sample corpus.

    Raises:
        FileNotFoundError: If the sample corpus file does not exist.
    """
    filepath = os.path.join("data", "sample_corpus.txt")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            "Sample corpus not found. Run scripts/download_sample_data.py first."
        )
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    return lines