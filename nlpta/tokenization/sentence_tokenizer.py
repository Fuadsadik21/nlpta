import re

SENTENCE_ENDINGS = r"[.!?።፧፨]"

def sentence_tokenize(text: str) -> list:
    """
    Splits text into sentences using punctuation rules.
    """
    if not text or not text.strip():
        return []

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text.strip())

    # Split while keeping punctuation
    sentences = re.split(f"({SENTENCE_ENDINGS})", text)

    results = []
    buffer = ""

    for part in sentences:
        buffer += part
        if re.match(SENTENCE_ENDINGS, part):
            results.append(buffer.strip())
            buffer = ""

    if buffer.strip():
        results.append(buffer.strip())

    return results
