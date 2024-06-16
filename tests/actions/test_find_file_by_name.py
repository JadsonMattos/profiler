# ----------------------------------------------------------------------------
# Testes implementados pela Trybe
# ----------------------------------------------------------------------------


import pytest

from pro_filer.actions.beta_actions import find_file_by_name
from pro_filer.entities import Context

pytestmark = pytest.mark.dependency()


@pytest.fixture
def base_context() -> Context:
    return {
        "base_path": "any",
        "all_dirs": [],
        "all_files": [
            "/path/to/file.sql",
            "/path/to/file.txt",
            "/path/to/file2.txt",
            "/path/to/FILE.txt",
            "/path/to/FILE2.TXT",
            "/path/to/something.txt",
            "/path-to/file.txt",
        ],
    }


@pytest.mark.parametrize(
    "name, expected",
    [
        (
            "file",
            [
                "/path/to/file.sql",
                "/path/to/file.txt",
                "/path/to/file2.txt",
                "/path-to/file.txt",
            ],
        ),
        ("FILE", ["/path/to/FILE.txt", "/path/to/FILE2.TXT"]),
        ("something", ["/path/to/something.txt"]),
        (
            "txt",
            [
                "/path/to/file.txt",
                "/path/to/file2.txt",
                "/path/to/FILE.txt",
                "/path/to/something.txt",
                "/path-to/file.txt",
            ],
        ),
    ],
)
def test_valid_path_case_sensitive(base_context, name, expected):
    assert find_file_by_name(base_context, name) == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        (
            "file",
            [
                "/path/to/file.sql",
                "/path/to/file.txt",
                "/path/to/file2.txt",
                "/path/to/FILE.txt",
                "/path/to/FILE2.TXT",
                "/path-to/file.txt",
            ],
        ),
        (
            "FILE",
            [
                "/path/to/file.sql",
                "/path/to/file.txt",
                "/path/to/file2.txt",
                "/path/to/FILE.txt",
                "/path/to/FILE2.TXT",
                "/path-to/file.txt",
            ],
        ),
        ("something", ["/path/to/something.txt"]),
    ],
)
def test_valid_path_case_insensitive(base_context, name, expected):
    assert (
        find_file_by_name(base_context, name, case_sensitive=False) == expected
    )


@pytest.mark.parametrize("name", ["invalid", "path", "exe", ""])
def test_invalid_paths(base_context, name):
    assert find_file_by_name(base_context, name) == []
    assert find_file_by_name(base_context, name, case_sensitive=False) == []


@pytest.mark.dependency(
    depends=[
        "test_valid_path_case_sensitive",
        "test_valid_path_case_insensitive",
        "test_invalid_paths",
    ]
)
def test_find_file_by_name_final():
    pass
