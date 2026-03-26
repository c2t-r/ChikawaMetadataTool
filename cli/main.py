import argparse
from pathlib import Path

from cli.decrypt import decrypt_metadata


def main() -> None:
    parser = argparse.ArgumentParser(description="Decrypt chikawa metadata.")
    parser.add_argument("input", type=Path, help="Path to global-metadata.dat")
    args = parser.parse_args()

    input_path: Path = args.input
    decrypted = decrypt_metadata(input_path)

    output_path = input_path.parent / ("decrypted-" + input_path.name)
    with open(output_path, "wb") as f:
        f.write(decrypted)
