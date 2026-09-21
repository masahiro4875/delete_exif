from pathlib import Path
from processor import process_directory


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    input_dir = project_root / "tests" / "test_images"
    output_dir = input_dir / "output"

    process_directory(input_dir, output_dir)


if __name__ == "__main__":
    main()
