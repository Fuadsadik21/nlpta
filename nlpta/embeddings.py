import os
from gensim.models import Word2Vec

def load_embeddings():
    """Load pretrained Word2Vec embeddings."""
    model_path = os.path.join("data", "embeddings.bin")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            "Embeddings not found. Run scripts/train_embeddings.py first."
        )
    
    model = Word2Vec.load(model_path)
    return model