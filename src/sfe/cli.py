import argparse
import sys

from sfe.crypto import encrypt, decrypt
from sfe.kdf import derive_key, generate_salt
from sfe.utils import read_file, write_file, pack_data, unpack_data
from sfe.exceptions import DecryptionError

def encrypt_file(input_path, output_path, password):
    data = read_file(input_path)

    salt = generate_salt()
    key = derive_key(password, salt)

    encrypted = encrypt(data, key)
    blob = pack_data(salt, encrypted)

    write_file(output_path, blob)
    print(f"Encrypted -> {output_path}")


def decrypt_file(input_path, output_path, password):
    blob = read_file(input_path)

    try:
        salt, encrypted = unpack_data(blob)
        key = derive_key(password, salt)

        plaintext = decrypt(encrypted, key)

        write_file(output_path, plaintext)
        print(f"Decrypted -> {output_path}")

    except DecryptionError:
        print("Error: Decryption failed (wrong password or tampered data)")
        sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Secure File Encryption Tool")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encrypt
    enc_parser = subparsers.add_parser("encrypt")
    enc_parser.add_argument("input")
    enc_parser.add_argument("output")
    enc_parser.add_argument("-p", "--password", required=True)

    # Decrypt
    dec_parser = subparsers.add_parser("decrypt")
    dec_parser.add_argument("input")
    dec_parser.add_argument("output")
    dec_parser.add_argument("-p", "--password", required=True)

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt_file(args.input, args.output, args.password)

    elif args.command == "decrypt":
        decrypt_file(args.input, args.output, args.password)


if __name__ == "__main__":
    main()