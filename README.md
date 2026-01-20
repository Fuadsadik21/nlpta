# NLPTA

NLPTA is a Python toolkit for Amharic Natural Language Processing (NLP).
It provides standardized preprocessing, dataset utilities, and model
interfaces tailored to the linguistic properties of Amharic.

## Why Amharic NLP?
Amharic is morphologically rich and under-resourced.
Generic NLP tools often fail to handle its script variations,
tokenization rules, and morphology correctly.

NLPTA aims to provide a reliable and extensible foundation for
Amharic NLP research and applications.

## Installation
pip install nlpta

## Quick Example
```python
import nlpta

text = "አማርኛ ጽሑፍ"
tokens = nlpta.tokenize(text)
