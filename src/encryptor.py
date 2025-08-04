# === encryption + encoding module ===
# Purpose: Encrypt a Python code string and obfuscate it visually using two novelty layers:
# - Wingding-style symbolic encoding (not real Wingdings, just fake glyphs)
# - Greeklish character substitution (visual, not semantic)
# Intended for experimental use in novelty obfuscation projects.

from cryptography.fernet import Fernet  # Symmetric encryption class from cryptography lib
from utils.fonts import wingify         # Custom function to symbolically encode text
from utils.greeklish import greeklishify  # Custom function to apply Greek-style transliteration

# Function: Generate a symmetric key for Fernet encryption
def generate_key() -> bytes:
    """
    Generates a secure random Fernet encryption key.
    Returns:
        bytes: A 32-byte URL-safe base64-encoded key.
    """
    return Fernet.generate_key()

# Function: Encrypt a string of code using Fernet symmetric encryption
def encrypt_code(code: str, key: bytes) -> bytes:
    """
    Encrypts a plaintext string using the provided Fernet key.
    
    Args:
        code (str): The source code or plaintext to encrypt.
        key (bytes): A Fernet-compatible symmetric key.

    Returns:
        bytes: The encrypted ciphertext.
    """
    fernet = Fernet(key)          # Instantiate a Fernet cipher suite with the key
    return fernet.encrypt(code.encode())  # Encode string to bytes, then encrypt

# Script Entry Point: Only runs when this file is executed directly
if __name__ == "__main__":
    # === STEP 1: Write plaintext Python code to be encrypted ===
    original_code = '''
def secret_app():
    msg = input("Enter a message: ")
    print("You said:", msg)

secret_app()
'''

    # === STEP 2: Generate a new random symmetric key ===
    key = generate_key()  # Key must be securely saved to allow decryption later

    # === STEP 3: Encrypt the code using the generated key ===
    encrypted = encrypt_code(original_code, key)

    # === STEP 4: Obfuscate the encrypted bytes into Wingding-like symbols ===
    wingding_encoded = wingify(encrypted)

    # === STEP 5: Apply Greeklish transformation for extra visual flair ===
    greek_display = greeklishify(wingding_encoded)

    # === OUTPUT SECTION: Print results ===
    print("=== SAVE THIS KEY ===")
    print(key.decode())  # Key is output as a UTF-8 string for storage or reuse

    print("\n=== Wingdings Encoded ===")
    print(wingding_encoded)  # Encrypted data, visually obfuscated

    print("\n=== Greeklishified Preview ===")
    print(greek_display)     # Visually mangled version for display only
