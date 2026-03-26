from pathlib import Path

from src.key import KEY


def decrypt_metadata(input_path: Path) -> bytes:
    with open(input_path, "rb") as f:
        data = bytearray(f.read())

    for i in range(len(data)):
        data[i] ^= KEY[i % 128]

    return bytes(data)
