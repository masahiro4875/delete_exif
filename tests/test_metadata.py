from PIL import Image
from PIL.PngImagePlugin import PngInfo

from delete_exif.metadata import remove_metadata

delete_keys = {"Description", "Software", "Source", "Generation time", "Comment"}


def test_removes_comment_and_keeps_author(tmp_path):
    input_path = tmp_path / "input.png"
    output_path = tmp_path / "output" / "result.png"

    metadata = PngInfo()

    # テストする画像データに付加するメタデータ
    metadata.add_text("Description", "test description")
    metadata.add_text("Software", "test software")
    metadata.add_text("Source", "test source")
    metadata.add_text("Generation time", "test generation time")
    metadata.add_text("Comment", "test commnet")
    metadata.add_text("Title", "test title")

    Image.new("RGB", (10, 10), color="red").save(
        input_path,
        pnginfo=metadata,
    )

    remove_metadata(input_path, output_path)

    with Image.open(output_path) as image:
        for key in delete_keys:
            assert key not in image.info
            assert image.info["Title"] == "test title"
            assert image.size == (10, 10)
