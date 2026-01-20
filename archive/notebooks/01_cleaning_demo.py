from nlpta import load_sample_corpus, clean_text
from nlpta.tokenization import tokenize

def main():
    print("📥 Loading sample Amharic corpus...")
    corpus = load_sample_corpus()
    print(f"✅ Loaded {len(corpus)} paragraphs.\n")

    print("=" * 80)
    print("🧹 CLEANING DEMO: First 3 Paragraphs")
    print("=" * 80)

    for i, paragraph in enumerate(corpus[:3]):
        print(f"\n📄 Paragraph {i+1} (Original):")
        print("-" * 40)
        print(paragraph[:200] + "..." if len(paragraph) > 200 else paragraph)

        print(f"\n✨ Paragraph {i+1} (Cleaned):")
        print("-" * 40)
        cleaned = clean_text(paragraph)
        print(cleaned[:200] + "..." if len(cleaned) > 200 else cleaned)

        print("\n" + "=" * 80)
        print(f"\n🔍 Paragraph {i+1} (Tokens):")
        print("-" * 40)
        tokens = tokenize(cleaned)
        print(tokens[:10])  # Show first 10 tokens
        print(f"\n🚫 Paragraph {i+1} (After Stopword Removal):")
        print("-" * 40)
        no_stops = remove_stopwords(tokens)
        print(no_stops[:10])  # Show first 10 tokens

if __name__ == "__main__":
    main()