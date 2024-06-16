from datetime import date
import os
import re
import pytest
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_messages(capsys):
    context = {
        "base_path": "images/pro-filer-preview.gif"
    }
    show_details(context)
    captured = capsys.readouterr()
    assert "File name: " in captured.out
    assert "File size in bytes: " in captured.out
    assert "File type: " in captured.out
    assert "File extension: " in captured.out
    assert "Last modified date: " in captured.out


def test_show_details_incorrect_date(capsys):
    context = {
        "base_path": "images/pro-filer-preview.gif"
    }
    show_details(context)
    captured = capsys.readouterr()
    assert re.search(r"Last modified date: \d{4}-\d{2}-\d{2}\n",
                     captured.out) is not None


def test_show_details_no_file(capsys):
    context = {
        "base_path": "images/????"
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"


@pytest.fixture
def file_without_extension(tmp_path):
    file_path = tmp_path / "file_without_extension"
    file_path.write_text("This is a test file without extension.")
    return str(file_path)


def test_show_details_file_without_extension(file_without_extension, capsys):
    context = {"base_path": file_without_extension}
    show_details(context)
    captured = capsys.readouterr()
    assert "File extension: [no extension]" in captured.out


def test_show_details_file(capsys):
    context = {
        "base_path": "images/pro-filer-preview.gif"
    }
    show_details(context)
    file_size = os.path.getsize(context["base_path"])
    file_type = 'file'
    file_extension = '.gif'
    last_modified_date = date.fromtimestamp(
        os.path.getmtime(context["base_path"]))
    captured = capsys.readouterr()
    assert captured.out == f"File name: pro-filer-preview.gif\nFile size in \
bytes: {file_size}\nFile type: {file_type}\nFile extension: \
{file_extension}\nLast modified date: {last_modified_date}\n"
