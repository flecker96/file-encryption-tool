import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from sfe.exceptions import DecryptionError, EncryptionError


NONCE_SIZE = 12        # Recommended size for GCM
KEY_SIZE = 32          # 256-bit AES
TAG_SIZE = 16          # GCM tag is 16 bytes


def generate_nonce() -> bytes:
    """
    Generate a secure random nonce for AES-GCM.
    """
    return os.urandom(NONCE_SIZE)


def encrypt(data: bytes, key: bytes, associated_data: bytes = None) -> bytes:
    """
    Encrypt data using AES-GCM.

    Args:
        data: plaintext bytes
        key: 32-byte encryption key
        associated_data: optional additional authenticated data (AAD)

    Returns:
        nonce + ciphertext (ciphertext already includes authentication tag)
    """
    if len(key) != KEY_SIZE:
        raise EncryptionError("Key must be 32 bytes (256-bit)")

    try:
        aesgcm = AESGCM(key)
        nonce = generate_nonce()

        ciphertext = aesgcm.encrypt(nonce, data, associated_data)

        # Output format: [nonce | ciphertext+tag]
        return nonce + ciphertext

    except Exception as e:
        raise EncryptionError(f"Encryption failed: {e}")


def decrypt(encrypted_data: bytes, key: bytes, associated_data: bytes = None) -> bytes:
    """
    Decrypt data using AES-GCM.

    Args:
        encrypted_data: nonce + ciphertext (+ tag)
        key: 32-byte encryption key
        associated_data: must match encryption AAD

    Returns:
        plaintext bytes

    Raises:
        DecryptionError if authentication fails
    """
    if len(key) != KEY_SIZE:
        raise DecryptionError("Key must be 32 bytes (256-bit)")

    if len(encrypted_data) < NONCE_SIZE:
        raise DecryptionError("Invalid encrypted data")

    try:
        nonce = encrypted_data[:NONCE_SIZE]
        ciphertext = encrypted_data[NONCE_SIZE:]

        aesgcm = AESGCM(key)

        # Will raise exception if authentication fails
        plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data)

        return plaintext

    except Exception:
        # Do NOT leak details → important security practice
        raise DecryptionError("Decryption failed (possible tampering or wrong key)")