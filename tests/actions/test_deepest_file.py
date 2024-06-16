# ----------------------------------------------------------------------------
# Testes implementados pela Trybe
# ----------------------------------------------------------------------------

from faker import Faker
import pytest
from pro_filer.actions.beta_actions import show_deepest_file

pytestmark = pytest.mark.dependency()


def test_deepest_file_with_no_files_to_analyze(capsys):
    context = {"all_files": []}
    show_deepest_file(context)
    captured = capsys.readouterr()
    assert captured.out == "No files found\n"


def test_single_file_should_be_deepest_file(capsys, faker: Faker):
    mock_file_path = faker.file_path()
    context = {
        "all_files": [
            mock_file_path,
        ]
    }
    show_deepest_file(context)
    captured = capsys.readouterr()
    assert captured.out == f"Deepest file: {mock_file_path}\n"


def test_should_decide_deepest_file_by_directory_depth(capsys):
    deep_file_path = "this/file/is/a/very/deep/file.txt"
    shallow_file_path = "this/is/a/shallow/file_with_big_name.txt"
    context = {
        "all_files": [
            deep_file_path,
            shallow_file_path,
        ]
    }
    show_deepest_file(context)
    captured = capsys.readouterr()
    assert captured.out == f"Deepest file: {deep_file_path}\n"


@pytest.mark.dependency(
    depends=[
        "test_should_decide_deepest_file_by_directory_depth",
        "test_deepest_file_with_no_files_to_analyze",
        "test_single_file_should_be_deepest_file",
    ]
)
def test_deepest_file_final():
    pass
