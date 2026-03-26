from pathlib import Path

from cli.key import KEY


def decrypt_metadata(input_path: Path) -> bytes:
    with open(input_path, "rb") as f:
        data = bytearray(f.read())

    for i in range(len(data)):
        data[i] ^= KEY[i % 128]

    return bytes(data)
