from nlpta import load_embeddings

def test_load_embeddings():
    model = load_embeddings()
    assert model is not None
    
    # Test vocabulary
    # Check if word exists in vocabulary
    assert "ኢትዮጵያ" in model.wv.key_to_index
    assert "አበባ" in model.wv
    
    # Test vector shape
    vec = model.wv["ኢትዮጵያ"]
    assert len(vec) == 100  # default vector_size