import sys
from pathlib import Path

from src.decrypt import decrypt_metadata


def main() -> None:
    if len(sys.argv) < 2:
        print("Only 1 arg accepted. <global-metadata.dat>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    decrypted = decrypt_metadata(input_path)

    output_path = input_path.parent / ("decrpted-" + input_path.name)
    with open(output_path, "wb") as f:
        f.write(decrypted)
