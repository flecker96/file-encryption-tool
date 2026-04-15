import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

SALT_SIZE = 16
ITERATIONS = 200_000
KEY_SIZE = 32  # gives a 256-bit key


def generate_salt() -> bytes:
    return os.urandom(SALT_SIZE)


def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive a cryptographic key from a password by PBKDF2.
    (applying hash-f. to password+salt ITERATIONS times)
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
    )
    return kdf.derive(password.encode())