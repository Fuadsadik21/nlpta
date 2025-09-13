from gensim.models import Word2Vec
from nlpta import load_sample_corpus, tokenize, remove_stopwords, load_stopwords
import os

def train_word2vec(corpus, vector_size=100, window=5, min_count=1, workers=4):
    """
    Train Word2Vec embeddings on Amharic text.
    """
    print("🧹 Preprocessing corpus...")
    stopwords = load_stopwords()
    sentences = []
    for text in corpus:
        tokens = tokenize(text)
        tokens = remove_stopwords(tokens, stopwords)
        if len(tokens) > 1:  # Only keep sentences with 2+ tokens
            sentences.append(tokens)
    
    print(f"📚 Training on {len(sentences)} sentences...")
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=workers,
        sg=1  # Skip-gram (better for smaller corpora)
    )
    
    return model

def main():
    # Load corpus
    corpus = load_sample_corpus()
    
    # Train model
    model = train_word2vec(corpus)
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Save model
    model_path = "data/embeddings.bin"
    model.save(model_path)
    print(f"✅ Model saved to {model_path}")
    
    # Test a few words
    print("\n🔍 Testing embeddings:")
    test_words = ["ኢትዮጵያ", "አዲስ", "አበባ", "ሕዝብ", "መንግሥት"]
    for word in test_words:
        if word in model.wv:
            print(f"  {word}: {model.wv[word][:5]}...")  # Show first 5 dimensions
        else:
            print(f"  {word}: Not in vocabulary")

if __name__ == "__main__":
    main()