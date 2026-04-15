class DecryptionError(Exception):
    """Raised when decryption fails or authentication fails."""
    pass

class EncryptionError(Exception):
    pass

#can in principle add more errors here if want model to be extended more