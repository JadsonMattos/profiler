import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


@pytest.fixture
def files_with_different_content(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("This is a test content for file1.")
    file2 = tmp_path / "file2.txt"
    file2.write_text("This is a test content for file2.")
    file3 = tmp_path / "file3.txt"
    file3.write_text("This is a test content for file3.")
    return [str(file) for file in [file1, file2, file3]]


@pytest.fixture
def non_existing_file(tmp_path):
    return str(tmp_path / "non_existing_file.txt")


def test_find_duplicate_files_differents(files_with_different_content):
    context = {"all_files": files_with_different_content}
    assert find_duplicate_files(context) == []


def test_find_duplicate_files_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("This is a test content.")
    file2 = tmp_path / "file2.txt"
    file2.write_text("This is a test content.")
    file3 = tmp_path / "file3.txt"
    file3.write_text("This is a test content.")

    context = {"all_files": [str(file) for file in [file1, file2, file3]]}
    assert find_duplicate_files(context) == [
        (str(file1), str(file2)), (str(file1), str(file3)),
        (str(file2), str(file3))
    ]


def test_find_duplicate_files_non_existing_file(non_existing_file):
    context = {"all_files": ["existing_file.txt", non_existing_file]}
    with pytest.raises(ValueError):
        find_duplicate_files(context)
