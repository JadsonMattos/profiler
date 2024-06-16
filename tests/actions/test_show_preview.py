from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_no_files_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_more_five_files_dirs(capsys):
    context = {
        "all_files": ["file1", "file2", "file3", "file4", "file5", "file6"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 6 files and 6 directories\nFirst 5 files: \
['file1', 'file2', 'file3', 'file4', 'file5']\nFirst 5 directories: \
['dir1', 'dir2', 'dir3', 'dir4', 'dir5']\n"


def test_show_preview_files_dirs(capsys):
    context = {
        "all_files": ["file1", "file2", "file3"],
        "all_dirs": ["dir1", "dir2"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 3 files and 2 directories\nFirst 5 files: \
['file1', 'file2', 'file3']\nFirst 5 directories: ['dir1', 'dir2']\n"
