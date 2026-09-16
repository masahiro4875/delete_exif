from pathlib import Path

from PIL import Image
from PIL.PngImagePlugin import PngInfo

delete_keys = {"Description", "Software", "Source", "Generation time", "Comment"}


def remove_metadata(input_path: Path, output_path: Path) -> None:

    with Image.open(input_path) as image:
        metadata = PngInfo()

        for key, value in image.info.items():
            if key not in delete_keys and isinstance(value, str):
                metadata.add_text(key, value)

        pixels = image.copy()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pixels.save(output_path, format="PNG", pnginfo=metadata)

if __name__ == "__main__":
    input_path = Path("tests/test_images/test.png")
    output_path = Path("tests/test_images/output_test.png")

    remove_metadata(input_path, output_path)

