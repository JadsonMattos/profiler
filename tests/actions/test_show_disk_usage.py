import os
import pytest
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


@pytest.fixture
def files_with_size(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("This is a test.")
    file2 = tmp_path / "file2.txt"
    file2.write_text("This is another test.")
    file3 = tmp_path / "file3.txt"
    file3.write_text("This is yet another test.")
    file4 = tmp_path / "file4.txt"
    file4.write_text("This is the last test.")
    return [str(file) for file in [file1, file2, file3, file4]]


@pytest.fixture
def empty_dir(tmp_path):
    return str(tmp_path)


@pytest.fixture
def file_sizes(files_with_size):
    return [os.path.getsize(file) for file in files_with_size]


def test_show_disk_usage_incorrect_total_size(files_with_size, capsys):
    context = {"all_files": files_with_size}
    show_disk_usage(context)
    captured = capsys.readouterr()
    total_size = int(captured.out.split("Total size:")[1].strip())
    assert total_size == sum(os.path.getsize(file) for file in files_with_size)


def test_show_disk_usage_empty(empty_dir, capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert "Total size: 0" in captured.out


def test_show_disk_usage_order_by_size(files_with_size, file_sizes, capsys):
    context = {"all_files": files_with_size}
    show_disk_usage(context)
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert len(lines) == len(file_sizes) + 1
    sizes_from_output = [
        int(line.split("(")[0].strip().split()[-1]) for line in lines[:-1]
    ]
    sorted_file_sizes = sorted(file_sizes, reverse=True)
    assert sorted_file_sizes == sizes_from_output


def test_show_disk_usage_files_with_size(files_with_size, capsys):
    context = {"all_files": files_with_size}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert "Total size:" in captured.out
    assert "file1.txt" in captured.out
    assert "file2.txt" in captured.out
    assert "file3.txt" in captured.out
