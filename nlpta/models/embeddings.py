import os
from gensim.models import Word2Vec

def load_embeddings(path):
    """
    Load word embeddings from a file.

    Args:
        path (str): Path to the embeddings file.

    Returns:
        dict: A dictionary mapping words to their embedding vectors.
    """
    model_path = os.path.join("data", "embeddings.bin")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            "Embeddings not found. Run scripts/train_embeddings.py first."
        )
    
    model = Word2Vec.load(model_path)
    return model

def get_embedding(word, embeddings):
    """
    Retrieve the embedding vector for a given word.

    Args:
        word (str): The word to look up.
        embeddings (dict): The embeddings dictionary.

    Returns:
        np.ndarray or None: The embedding vector, or None if not found.
    """
    try:
        return embeddings.wv[word]
    except KeyError:
        return None