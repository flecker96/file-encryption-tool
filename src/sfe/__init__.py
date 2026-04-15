"""Secure File Encryption (SFE) package."""

__version__ = "0.1.0"

from .crypto import encrypt, decrypt
from .kdf import derive_key

__all__ = ["encrypt", "decrypt", "derive_key"]