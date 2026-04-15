# Format for packing data into .enc file:
# [salt (16 bytes)] [encrypted_data]

SALT_SIZE = 16


def pack_data(salt: bytes, encrypted_data: bytes) -> bytes:
    return salt + encrypted_data


def unpack_data(blob: bytes):
    if len(blob) < SALT_SIZE:
        raise ValueError("Invalid data format")

    salt = blob[:SALT_SIZE]
    encrypted_data = blob[SALT_SIZE:]
    return salt, encrypted_data


def read_file(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def write_file(path: str, data: bytes):
    with open(path, "wb") as f:
        f.write(data)