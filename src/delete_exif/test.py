from pathlib import Path

from PIL import Image
from PIL.PngImagePlugin import PngInfo

# 画像読み込み
input_image_path = Path("tests/test_images/test.png")
output_image_path = Path("tests/test_images/output_test.png")
delete_keys = {"Description", "Software", "Source", "Generation time", "Comment"}

with Image.open(input_image_path) as image:
    # メタデータインスタンス作成
    metadata = PngInfo()

    for key, value in image.info.items():
        if key not in delete_keys and isinstance(value, str):
            metadata.add_text(key, value)

    pixels = image.copy()

pixels.save(output_image_path, format="PNG", pnginfo=metadata)

with Image.open(output_image_path) as image:
    print(image.info.items())
