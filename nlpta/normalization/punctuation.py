import re

def normalize_punctuation(text: str) -> str:
    """
    Normalizes punctuation for Amharic text.
    
    Removes non-linguistic symbols (e.g., @, #, $) and canonicalizes standard 
    Western punctuation (., ;:?) into their Amharic equivalents (። ፣ ፤ ፦ ፧). 
    Amharic-specific punctuation is preserved to maintain the structural 
    and rhythmic integrity of the language.
    """
    
    # 1. Define Canonicalization Mapping
    # Rule C: Convert Western to Amharic equivalents
    punctuation_map = {
        ".": "።",
        ",": "፣",
        ";": "፤",
        ":": "፦",
        "?": "፧"
    }
    
    # 2. Define removal set
    # Rule A: Symbols to remove completely (excluding those we map in Rule C)
    # Note: we handle the mapping first, then remove remaining Rule A symbols.
    to_remove = r'[!@#$%^&*()\[\]{}"\'/<>\… ]' # We keep spaces for readability
    
    # Perform mapping
    for western, amharic in punctuation_map.items():
        text = text.replace(western, amharic)
        
    # Rule A: Remove the rest of the non-linguistic symbols
    # We use a regex to strip symbols specified in the objective
    text = re.sub(r'[!@#\$%\^&\*\(\)\[\]{}"\'\/<>\?…]+', '', text)

    return text