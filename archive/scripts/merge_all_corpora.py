import os

def merge_all_corpora():
    """Merge all downloaded corpora into one big file."""
    files = [
        "data/sample_corpus.txt",          # Original Wikipedia
        "data/bbc_sample_corpus.txt",      # BBC headlines
        "data/bbc_full_articles.txt",      # BBC full articles
        "data/wikipedia_full_corpus.txt"   # Full Wikipedia pages
    ]
    
    all_lines = []
    for file_path in files:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                all_lines.extend(f.readlines())
    
    # Save merged corpus
    with open("data/merged_large_corpus.txt", "w", encoding="utf-8") as f:
        f.writelines(all_lines)
    
    print(f"✅ Merged {len(all_lines)} lines into data/merged_large_corpus.txt")

if __name__ == "__main__":
    merge_all_corpora()