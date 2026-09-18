from pathlib import Path

from .metadata import remove_metadata

delete_keys = {"Description", "Software", "Source", "Generation time", "Comment"}


def process_directory(
    input_dir: Path,
    output_dir: Path,
    delete_keys: str[str],
) -> None:

    for input_path in input_dir.glob("*.png"):
        output_path = output_dir / input_path.name

        remove_metadata(input_path=input_path, output_path=output_path)
