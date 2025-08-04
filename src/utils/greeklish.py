# === greeklish.py ===
# This module defines a function to simulate a Greeklish transformation.
# It replaces Latin letters with Greek-looking counterparts (visually similar, not accurate).
# This is for fun/obfuscation only.

def greeklishify(text: str) -> str:
    """
    Translates English capital letters to similar-looking Greek characters.
    This is a purely visual transformation.

    Args:
        text (str): A string of normal or wingdings-encoded text.

    Returns:
        str: A version with some letters replaced by Greek-ish lookalikes.
    """
    # Use str.maketrans to define a quick character-to-character substitution map
    greek_map = str.maketrans("ABEGIKMNOPRSTUXYZ", "ΑΒΕGΙΚΜΝΟΡRSTΥΧΥΖ")

    # Apply the translation using str.translate
    return text.translate(greek_map)
