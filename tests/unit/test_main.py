from unittest import skip
from unittest.mock import patch

from src import main


class DirEntry:
    def __init__(self, name, is_file):
        self.name = name
        self.is_file = is_file

    def name(self):
        return self.name

    def is_file(self):
        return self.is_file

    def path(self):
        return self.path


@patch("os.scandir")
def test_get_files(mock_scandir):
    valid_filenames = ["foo.wav", "bar.WAV", "baz.Wav"]
    invalid_filenames = ["foo.txt", "bar.mp3"]
    foldernames = [".", "..", "foo"]

    files_to_keep = [DirEntry(name, True) for name in valid_filenames]
    files_to_skip = [DirEntry(name, True) for name in invalid_filenames]
    folders = [DirEntry(name, False) for name in foldernames]

    directory_contents = files_to_keep + files_to_skip + folders

    mock_scandir.return_value = directory_contents

    expected_result = files_to_keep
    actual_result = main.get_files()

    assert actual_result == expected_result


@patch("AudioSegment.from_wav")
@patch("effects.normalize")
def test_normalize_audio(mock_normalize, mock_from_wav):
    mock_normalize.return_value = "blah"
    mock_from_wav.return_value = "blahblah"

    expected_result = True
    actual_result = main.normalize_audio("foo")

    assert actual_result == expected_result


def test_main():
    actual_result = main.main()

    expected_result = True
    assert actual_result == expected_result
