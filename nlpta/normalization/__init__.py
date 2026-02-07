"""
Normalization subpackage for NLPTA.

This package contains text normalization utilities specific to
Amharic (Ge'ez script), including punctuation, character variants,
whitespace, and numeral handling.

Modules
-------
- punctuation: Functions to normalize Amharic punctuation.
- whitespace: Functions to standardize whitespace in text.
- character_variants: Functions to normalize character variants.
- numerals: Functions to convert between Amharic and Arabic numerals.

"""
from .punctuation import normalize_punctuation
from .whitespace import normalize_whitespace
from .characters import normalize_characters
from .numerals import normalize_numerals
from .pipeline import normalize
__all__ = [
    "normalize_punctuation",
    "normalize_whitespace",
    "normalize_characters",
    "normalize_numerals",
    "normalize"]