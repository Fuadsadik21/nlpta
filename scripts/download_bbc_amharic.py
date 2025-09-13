import requests
from bs4 import BeautifulSoup
import os
import time

def get_article_text(url):
    """Extract full text from BBC Amharic article."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get article body
        paragraphs = []
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if len(text) > 30:
                paragraphs.append(text)
        
        return "\n".join(paragraphs)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def download_bbc_full_articles():
    """Download full articles from BBC Amharic."""
    base_url = "https://www.bbc.com/amharic"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        print("📥 Fetching BBC Amharic article links...")
        response = requests.get(base_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find article links
        article_links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/amharic/' in href and len(href.split('/')) > 3:
                full_url = href if href.startswith('http') else f"https://www.bbc.com{href}"
                article_links.append(full_url)
        
        # Deduplicate
        article_links = list(set(article_links))[:50]  # Limit to 50 for now
        
        print(f"🔗 Found {len(article_links)} articles. Fetching full text...")
        
        all_text = []
        for i, url in enumerate(article_links):
            print(f"  {i+1}/{len(article_links)}: {url}")
            text = get_article_text(url)
            if text:
                all_text.append(text)
            time.sleep(1)  # Be respectful to server
        
        # Save
        os.makedirs("data", exist_ok=True)
        with open("data/bbc_full_articles.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(all_text))
        
        print(f"✅ Saved {len(all_text)} full articles to data/bbc_full_articles.txt")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_bbc_full_articles()