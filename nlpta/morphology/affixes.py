"""
Affix inventory for Amharic morphology.

Phase 3: Detection only.
This module defines the high-frequency prefixes and suffixes recognized by the NLPTA toolkit.
No stripping, stemming, or transformation logic is performed here. 

These lists are conservative to prevent over-stemming (stripping root letters).
"""

# nlpta/morphology/affixes.py

# Affix inventories
PREFIXES = ["በ", "ለ", "ከ", "የ", "እንደ", "እስከ"]
SUFFIXES = ["ኝ", "ህ", "ሽ", "ው", "ች", "ነት"]

# Prefix role mappings
PREFIX_ROLES = {
    "በ": ["locative", "instrumental"],
    "ለ": ["dative", "benefactive"],
    "ከ": ["ablative", "source"],
    "የ": ["genitive", "possessive"],
    "እንደ": ["comparative", "manner"],
    "እስከ": ["temporal_limit", "spatial_limit"]
}

# Suffix role mappings
SUFFIX_ROLES = {
    "ኝ": ["1st_person_object"],
    "ህ": ["2nd_person_masc_possessive"],
    "ሽ": ["2nd_person_fem_possessive"],
    "ው": ["3rd_person_masc_object"],
    "ች": ["plural_feminine"],
    "ነት": ["abstract_noun"]
}

def detect_affixes(token):
    """
    Detect affixes in an Amharic token and tag them with possible grammatical roles.
    
    Args:
        token: String containing an Amharic token
        
    Returns:
        Dictionary with token, prefixes list, and suffixes list
    """
    result = {
        "token": token,
        "prefixes": [],
        "suffixes": []
    }
    
    # Detect prefixes
    for prefix in PREFIXES:
        if token.startswith(prefix):
            result["prefixes"].append({
                "form": prefix,
                "category": "prepositions",
                "roles": PREFIX_ROLES.get(prefix, [])
            })
    
    # Detect suffixes
    for suffix in SUFFIXES:
        if token.endswith(suffix):
            result["suffixes"].append({
                "form": suffix,
                "category": "possessive",  # Default category for suffixes
                "roles": SUFFIX_ROLES.get(suffix, [])
            })
    
    return result