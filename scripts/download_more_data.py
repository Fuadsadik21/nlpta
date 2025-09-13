import requests
from bs4 import BeautifulSoup
import os

def download_bbc_amharic():
    """Download sample news from BBC Amharic."""
    url = "https://www.bbc.com/amharic"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        print("📥 Fetching BBC Amharic News...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract article titles and summaries
        articles = []
        for item in soup.find_all('div', class_='gs-c-promo-heading'):
            title = item.get_text().strip()
            if len(title) > 20:
                articles.append(title)

        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)

        # Save to file
        output_path = "data/bbc_sample_corpus.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(articles))

        print(f"✅ Saved {len(articles)} articles to {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_bbc_amharic()