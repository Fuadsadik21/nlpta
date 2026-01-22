import re

def normalize_whitespace(text: str) -> str:
    """
    Standardize whitespace by collapsing multiple spaces, tabs, and newlines 
    into a single space and trimming leading/trailing ends.
    
    Safe on empty or None-like inputs. Does not interfere with Amharic 
    punctuation characters themselves, only the whitespace surrounding them.
    """
    # Guard clause: return input if it's None, empty string, or not a string
    if not text or not isinstance(text, str):
        return text

    # 1. Collapse multiple whitespaces (includes \t, \n, \r) into a single space
    # 2. Strip leading and trailing whitespace
    return re.sub(r'\s+', ' ', text).strip()