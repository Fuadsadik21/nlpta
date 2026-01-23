import re

def segment_sentences(text: str) -> list[str]:
    """
    Segments normalized Amharic text into sentences using Amharic sentence-ending punctuation.
    
    Parameters:
    text (str): The normalized Amharic text to segment.
    
    Returns:
    list[str]: An ordered list of sentences.
    """
    # Define the pattern to match Amharic sentence-ending punctuation
    sentence_end_pattern = r'[፧።?]|፨'
    
    # Split the text by sentence-ending punctuation
    sentences = re.split(sentence_end_pattern, text)
    
    # Filter out empty sentences and trim leading/trailing whitespace
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Reattach the punctuation marks to the end of each sentence
    punctuation_marks = re.findall(sentence_end_pattern, text)
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(punctuation_marks):
            result.append(sentence + punctuation_marks[i])
        else:
            result.append(sentence)
    
    return result

