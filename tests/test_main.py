from unittest.mock import patch
from delete_exif import main


def test_main_passes_correct_directories(tmp_path, monkeypatch):
    fake_file = tmp_path / "src" / "delete_exif" / "main.py"
    monkeypatch.setattr(main, "__file__", str(fake_file))

    with patch.object(main, "process_directory") as mock_process:
        main.main()

    mock_process.assert_called_once_with(
        tmp_path / "tests" / "test_images",
        tmp_path / "tests" / "test_images" / "output",
    )
    
