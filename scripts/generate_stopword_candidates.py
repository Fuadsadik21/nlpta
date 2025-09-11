# scripts/generate_stopword_candidates.py
from collections import Counter
from nlpta import load_sample_corpus, tokenize

def generate_word_frequencies(corpus):
    all_tokens = []
    for text in corpus:
        tokens = tokenize(text)
        all_tokens.extend(tokens)
    freq = Counter(all_tokens)
    return freq.most_common()

def main():
    print("📥 Loading corpus...")
    corpus = load_sample_corpus()
    
    print("📊 Generating word frequencies...")
    word_freq = generate_word_frequencies(corpus)
    
    output_path = "data/stopword_candidates.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Candidate stopwords (top 100 most frequent words)\n")
        f.write("# Review and remove words that carry MEANING\n")
        f.write("# Keep grammatical/functional words\n")
        f.write("# Format: word\tfrequency\n\n")
        for word, count in word_freq[:100]:
            f.write(f"{word}\t{count}\n")
    
    print(f"✅ Saved 100 candidates to {output_path}")
    print("\n➡️ NEXT: Open this file and curate your final stopword list.")

if __name__ == "__main__":
    main()