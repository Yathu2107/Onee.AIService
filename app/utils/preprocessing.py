import re


def clean_text(text: str) -> str:
    """
    Clean and normalize user input before tokenization.
    """

    if not text:
        return ""

    # Remove leading/trailing spaces
    text = text.strip()

    # Replace multiple spaces with one
    text = re.sub(r"\s+", " ", text)

    return text