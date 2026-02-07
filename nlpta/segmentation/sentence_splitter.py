# nlpta/segmentation/sentence_splitter.py

import re

def split_sentences(text: str) -> list[str]:
    """
    Basic Amharic sentence splitter.
    Splits on sentence terminators (። ፧ !) respecting abbreviations.
    
    Args:
        text: Input text string
        
    Returns:
        List of sentence strings
    """
    if not text or not text.strip():
        return []
    
    # Protect abbreviations from splitting
    # Pattern: letter.letter.letter. (e.g., ዓ.ም., እ.ኤ.አ.)
    abbreviation_pattern = r'([አ-ፈ]\.){2,}'
    
    # Temporarily replace abbreviations with placeholders
    placeholders = []
    def placeholder_replacer(match):
        placeholder = f"{{ABBR_{len(placeholders)}}}"
        placeholders.append(match.group())
        return placeholder
    
    protected_text = re.sub(abbreviation_pattern, placeholder_replacer, text)
    
    # Define sentence terminators
    # Capture the terminator in the split
    terminator_pattern = r'(።|፧|!)'
    
    # Split while keeping terminators
    segments = re.split(f'({terminator_pattern})', protected_text)
    
    # Reassemble sentences with their terminators
    sentences = []
    current = ""
    
    for segment in segments:
        if not segment:
            continue
        
        current += segment
        
        # If segment is a terminator, end the sentence
        if segment in '።፧!':
            # Restore any abbreviations in this sentence
            for i, abbr in enumerate(placeholders):
                current = current.replace(f"{{ABBR_{i}}}", abbr)
            
            # Clean up and add
            current = current.strip()
            if current:
                sentences.append(current)
                current = ""
    
    # Add any remaining text
    if current.strip():
        # Restore abbreviations
        for i, abbr in enumerate(placeholders):
            current = current.replace(f"{{ABBR_{i}}}", abbr)
        sentences.append(current.strip())
    
    # Handle ellipsis (።።።)
    merged = []
    i = 0
    while i < len(sentences):
        if i < len(sentences) - 2 and sentences[i+1] == "።" and sentences[i+2] == "።":
            # This is likely ellipsis, merge with current
            merged.append(sentences[i] + sentences[i+1] + sentences[i+2])
            i += 3
        else:
            merged.append(sentences[i])
            i += 1
    
    return merged


# Basic test
if __name__ == "__main__":
    test_cases = [
        "አለም ሰላም ነው። አዲስ ነገር መጣ።",
        "እንዴት ነህ፧ ሰላም ነኝ።",
        "በዓ.ነ.ግ. 2012 ተካሄደ። ፍጹም ነበር።",
        "ሰላም ነው።።። አሁን ሂዳለሁ።"
    ]
    
    for test in test_cases:
        print(f"Input:  {test}")
        print(f"Output: {split_sentences(test)}")
        print("-" * 50)