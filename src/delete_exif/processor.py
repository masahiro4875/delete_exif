from pathlib import Path

from PIL import Image
from PIL.PngImagePlugin import PngInfo

delete_keys = {"Description", "Software", "Source", "Generation time", "Comment"}


def process_directory(
        input_dir: Path,
        output_dir: Path,
        delete_keys: str[str],
        ) -> None:
    pass
