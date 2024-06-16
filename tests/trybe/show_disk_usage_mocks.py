from os import path
from pro_filer.cli_helpers import (
    _get_printable_file_path,
)
from pro_filer.actions import show_disk_usage
from pro_filer.entities import Context
from unittest.mock import patch

"""
def show_disk_usage(context: Context):
    total_size = sum(path.getsize(file) for file in context["all_files"])

    for file_path in sorted(
        context["all_files"], key=path.getsize, reverse=True
    ):
        file_size = path.getsize(file_path)
        print(
            f"'{_get_printable_file_path(file_path)}':".ljust(70),
            f"{file_size} ({int(file_size / total_size * 100)}%)",
        )

    print(f"Total size: {total_size}")
"""


def _test_wrong_total_size_calculation(context: Context):
    """E se o tamanho total ocupado pelos arquivos estiver errado?"""
    total_size = 0.1

    for file_path in sorted(
        context["all_files"], key=path.getsize, reverse=True
    ):
        file_size = path.getsize(file_path)
        print(
            f"'{_get_printable_file_path(file_path)}':".ljust(70),
            f"{file_size} ({int(file_size / total_size * 100)}%)",
        )

    print(f"Total size: {total_size}")


def _test_all_empty_files(context: Context):
    """E se a função achar que todos os arquivos estão vazios?"""
    with patch("pro_filer.actions.main_actions.path.getsize", lambda _: 0):
        show_disk_usage(context)


def _test_no_sorted_result(context: Context):
    """E se a saída não ordenar o resultado corretamente?"""

    def broken_sorted(data, **kwargs):
        kwargs["reverse"] = False
        return sorted(data, **kwargs)

    with patch("pro_filer.actions.main_actions.sorted", broken_sorted):
        show_disk_usage(context)
