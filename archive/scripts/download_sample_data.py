import requests
from bs4 import BeautifulSoup
import os

def download_amharic_sample():
    """
    Downloads sample Amharic text from Amharic Wikipedia.
    Saves to data/sample_corpus.txt
    """
    url = "https://am.wikipedia.org/wiki/ዋና_ገጽ"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        print("📥 Fetching Amharic Wikipedia...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all paragraph text
        paragraphs = []
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if len(text) > 20:  # Only keep meaningful paragraphs
                paragraphs.append(text)

        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)

        # Save to file
        output_path = "data/sample_corpus.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(paragraphs))

        print(f"✅ Saved {len(paragraphs)} paragraphs to {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_amharic_sample()