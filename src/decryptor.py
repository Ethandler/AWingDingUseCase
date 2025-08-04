# === decryptor.py ===
# This module is used to decrypt a Fernet-encrypted message using a known key.
# It reverses the actual encryption (but not the Wingdings or Greeklish stuff—they're just visual).

from cryptography.fernet import Fernet

def decrypt_code(encrypted: bytes, key: bytes) -> str:
    """
    Decrypts Fernet-encrypted data back into plaintext.

    Args:
        encrypted (bytes): The encrypted data (usually from Fernet).
        key (bytes): The original Fernet key used for encryption.

    Returns:
        str: The decrypted plaintext message.
    """
    fernet = Fernet(key)                  # Re-create the Fernet cipher with the saved key
    decrypted = fernet.decrypt(encrypted)  # Decrypt the bytes
    return decrypted.decode()             # Convert bytes back to a string
