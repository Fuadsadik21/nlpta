"""
Confidence assignments for Amharic affix surface-form detection.

Confidence reflects SURFACE-FORM DETECTION RELIABILITY,
NOT grammatical correctness or semantic plausibility.

Three levels:
- "high":   Unambiguous surface form, cannot appear stem-internally
- "medium": Common but can appear as part of a stem
- "low":    Very short forms that frequently appear inside stems

Rules:
- Conservative only. When in doubt, omit (defaults to medium).
- No academic speculation.
"""

# Default confidence for any affix not explicitly mapped
DEFAULT_CONFIDENCE = "medium"

# Mapping of each affix form to its confidence level
# Only includes clear high-confidence and low-confidence exceptions.
# Everything else defaults to medium.
AFFIX_CONFIDENCE = {
    # ==========================================
    # HIGH CONFIDENCE
    # Multi-char forms that cannot be stem-internal
    # ==========================================
    "እስከ": "high",  # Preposition: until
    "እንደ": "high",  # Preposition: like/as
    "ነት": "high",   # Suffix: abstract noun
    
    # ==========================================
    # LOW CONFIDENCE
    # Single-letter forms that are extremely common in roots
    # ==========================================
    "ይ": "low",     # Prefix: 3rd masc (single 'y')
    "ት": "low",     # Prefix: 3rd fem (single 't')
    "እ": "low",     # Prefix: 1st sing (single 'e')
    "ሽ": "low",     # Suffix: 2nd fem (very common in roots)
    "ም": "low",     # Suffix: extremely common in stems
    "ን": "low",     # Suffix: extremely common in stems
}

def get_confidence(affix_form: str) -> str:
    """
    Get the confidence level for a detected affix.
    
    Args:
        affix_form: The string form of the affix
        
    Returns:
        Confidence level: "high", "medium", or "low"
    """
    return AFFIX_CONFIDENCE.get(affix_form, DEFAULT_CONFIDENCE)