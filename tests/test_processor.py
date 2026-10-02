from PIL import Image
from PIL.PngImagePlugin import PngInfo


def test_delete_metadata_for_some_images(tmp_path):
    color_lists = ["red", "blue", "green"]
    input_dir = tmp_path / "input"
    output_dir = input_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    metadata = PngInfo()

    metadata.add_text("Description", "test description")
    metadata.add_text("Software", "test software")
    metadata.add_text("Source", "test source")
    metadata.add_text("Generation time", "test generation time")
    metadata.add_text("Comment", "test commnet")
    metadata.add_text("Title", "test title")

    for color_name in color_lists:
        Image.new("RGB", (10, 10), color=color_name).save(
            input_dir / "f{color_name}.png",
            pnginfo=metadata,
        )
