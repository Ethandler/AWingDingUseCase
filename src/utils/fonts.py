# === fonts.py ===
# This module defines a function to "Wingdings-ify" any text input.
# It replaces letters and numbers with visually fun or weird Unicode symbols,
# kind of like a homemade version of Wingdings.

# This dictionary maps common characters to symbols.
# These are just for looks – they don't actually mean anything different.
fake_wingding_map = {
    # Uppercase A-Z
    'A': '✈', 'B': '✉', 'C': '☂', 'D': '☎', 'E': '✔', 'F': '✖', 'G': '⚡', 'H': '♠', 'I': '♣',
    'J': '♥', 'K': '♦', 'L': '♫', 'M': '☯', 'N': '☠', 'O': '☢', 'P': '☣', 'Q': '☮', 'R': '♻',
    'S': '⚔', 'T': '⚖', 'U': '⚙', 'V': '✂', 'W': '✍', 'X': '⚓', 'Y': '⛓', 'Z': '✞',
    
    # Lowercase a-z
    'a': '☺', 'b': '☹', 'c': '☕', 'd': '⚙', 'e': '⚛', 'f': '⚜', 'g': '✝', 'h': '❄', 'i': '☃',
    'j': '❁', 'k': '❀', 'l': '✿', 'm': '⚘', 'n': '⚖', 'o': '⚔', 'p': '☄', 'q': '✧', 'r': '✩',
    's': '⚫', 't': '⚪', 'u': '⬤', 'v': '◉', 'w': '◌', 'x': '◍', 'y': '◯', 'z': '◎',

    # Digits 0–9
    '0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④', '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨'
}

def wingify(data: bytes) -> str:
    """
    Converts each letter/number in encrypted text to a fake symbol version.

    Args:
        data (bytes): Encrypted code (as bytes) from Fernet.

    Returns:
        str: Wingdings-style encoded string.
    """
    # First convert the bytes into a string so we can work with characters
    text = data.decode()

    # Build a new string, replacing each character using the fake_wingding_map
    # If the character isn't in the map (like "=" or "+"), it turns into '?'
    encoded = ''.join(fake_wingding_map.get(char, '?') for char in text)

    return encoded
