"""
Amharic Affix Detection Module.

Phase 3: Detection only.
This module identifies potential prefixes and suffixes based on surface-form matching.
It does NOT perform stripping, normalization, or disambiguation.
The input token is never mutated; a candidate stem is returned for informational purposes only.
"""

from .affixes import get_all_prefixes, get_all_suffixes

def detect_affixes(token: str) -> dict:
    """
    Analyzes a token to detect potential Amharic prefixes and suffixes.

    Args:
        token (str): The normalized word token to analyze.

    Returns:
        dict: A dictionary containing:
            - "token": The original input string.
            - "prefixes": List of all matching prefixes.
            - "suffixes": List of all matching suffixes.
            - "stem_candidate": A theoretical stem if affixes were removed 
                                (None if no affixes found or stem would be empty).
    """
    if not token:
        return {
            "token": token,
            "prefixes": [],
            "suffixes": [],
            "stem_candidate": None
        }

    # 1. Flatten inventories for detection
    all_prefixes = get_all_prefixes()
    all_suffixes = get_all_suffixes()

    # 2. Detect Prefixes (Check all possibilities)
    detected_prefixes = [p for p in all_prefixes if token.startswith(p)]

    # 3. Detect Suffixes (Check all possibilities)
    detected_suffixes = [s for s in all_suffixes if token.endswith(s)]

    # 4. Compute Stem Candidate (Informational Only)
    stem_candidate = None
    
    if detected_prefixes or detected_suffixes:
        # Strategy: Identify longest prefix and longest suffix for candidate generation
        # This is a heuristic for Phase 3 visualization, not final stemming logic.
        
        longest_prefix = ""
        if detected_prefixes:
            # Sort by length descending to find the longest match
            longest_prefix = sorted(detected_prefixes, key=len, reverse=True)[0]

        longest_suffix = ""
        if detected_suffixes:
            # Sort by length descending to find the longest match
            # Critical: Ensure the suffix isn't overlapping the prefix entirely in short words
            # (Simple check: stem shouldn't be empty)
            longest_suffix = sorted(detected_suffixes, key=len, reverse=True)[0]

        # Calculate the potential stem
        # Slice from end of prefix to start of suffix
        start_index = len(longest_prefix)
        end_index = len(token) - len(longest_suffix)

        # Sanity check: ensure we don't cross indices (e.g., prefix "abe", suffix "ebe" in "ab")
        if start_index < end_index:
            candidate = token[start_index:end_index]
            if candidate: # Ensure not empty
                stem_candidate = candidate

    return {
        "token": token,
        "prefixes": detected_prefixes,
        "suffixes": detected_suffixes,
        "stem_candidate": stem_candidate
    }