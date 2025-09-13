import wikipediaapi
import os

def download_wikipedia_corpus():
    """Download large corpus from Amharic Wikipedia."""
    wiki = wikipediaapi.Wikipedia(
        language='am',
        user_agent='nlpta-crawler (https://github.com/fuadsadik21/nlpta)'
    )
    
    # Get list of pages (you can expand this list)
    pages = [
        "ኢትዮጵያ", "አዲስ አበባ", "አማርኛ", "ኦሮሞ", "ትግራይ", "ሶማሊ", "አፋር",
        "ጎጃም", "ሻዋ", "ወሎ", "ቤተ ክርስቲያን", "እስልምና", "ጐሳ", "ትምህርት", "ጤና",
        "ኢኮኖሚ", "ፖለቲካ", "ታሪክ", "ባህል", "ሙዚቃ", "ፊልም", "ስፖርት", "ቴክኖሎጂ"
    ]
    
    all_text = []
    for page_title in pages:
        print(f"📥 Fetching: {page_title}")
        page = wiki.page(page_title)
        if page.exists():
            all_text.append(page.text)
        else:
            print(f"  ❌ Page not found: {page_title}")
    
    os.makedirs("data", exist_ok=True)
    with open("data/wikipedia_full_corpus.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(all_text))
    
    print(f"✅ Saved {len(pages)} Wikipedia pages.")

if __name__ == "__main__":
    download_wikipedia_corpus()