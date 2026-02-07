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


def load_dataset():
    """Load a simple placeholder dataset.

    This is a lightweight fallback used during development and testing
    when no external dataset loader is available.
    """
    return {
        "train": ["This is a training example."],
        "validation": ["This is a validation example."],
        "test": ["This is a test example."]
    }
def load_dataset ():
    """
    Load a dataset for NLP tasks.

    Returns:
        dict: A dictionary containing dataset splits (e.g., train, validation, test).
    """
    # Placeholder implementation
    dataset = {
        "train": ["This is a training example."],
        "validation": ["This is a validation example."],
        "test": ["This is a test example."]
    }
    return dataset