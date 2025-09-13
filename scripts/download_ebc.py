import requests
from bs4 import BeautifulSoup
import os

def download_ebc_articles():
    """Download articles from Ethiopian Broadcasting Corporation (EBC)."""
    base_url = "https://www.ebc.et"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        print("📥 Fetching EBC homepage...")
        response = requests.get(base_url + "/", headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article links
        article_links = set()
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('/Home/NewsDetails?NewsId='):
                article_links.add(base_url + href)

        print(f"🔗 Found {len(article_links)} article links.")

        articles = []
        for link in article_links:
            try:
                art_resp = requests.get(link, headers=headers, timeout=10)
                art_soup = BeautifulSoup(art_resp.content, 'html.parser')
                # Extract all <p> tags as article body
                paragraphs = [p.get_text().strip() for p in art_soup.find_all('p') if len(p.get_text().strip()) > 50]
                if paragraphs:
                    articles.append("\n".join(paragraphs))
            except Exception as e:
                print(f"❌ Error fetching {link}: {e}")

        os.makedirs("data", exist_ok=True)
        with open("data/ebc_articles.txt", "w", encoding="utf-8") as f:
            f.write("\n\n".join(articles))

        print(f"✅ Saved {len(articles)} EBC articles.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_ebc_articles()