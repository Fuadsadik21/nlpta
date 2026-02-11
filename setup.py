from setuptools import setup, find_packages

setup(
    name="nlpta",
    version="0.1.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Fuad Sadik",
    description="NLP Toolkit for Amharic",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fuadsadik21/nlpta",
    python_requires=">=3.7",
)
