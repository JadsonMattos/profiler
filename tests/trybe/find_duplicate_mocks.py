import filecmp
import itertools
from pro_filer.entities import Context
from pro_filer.actions.main_actions import find_duplicate_files


"""
def find_duplicate_files(context):
    all_files = context["all_files"]
    duplicate_files = []

    for file1, file2 in itertools.combinations(all_files, 2):
        try:
            if filecmp.cmp(file1, file2, shallow=False):
                duplicate_files.append((file1, file2))
        except FileNotFoundError:
            raise ValueError("All files must exist")

    return duplicate_files
"""


def _test_all_file_are_the_same(context: Context):
    """E se todos os arquivos forem considerados iguais?"""

    all_files = context["all_files"]
    duplicate_files = []

    for file1, file2 in itertools.combinations(all_files, 2):
        try:
            if filecmp.cmp(file1, file2, shallow=False) or True:
                duplicate_files.append((file1, file2))
        except FileNotFoundError:
            raise ValueError("All files must exist")

    return duplicate_files


def _test_none_are_duplicate(context: Context):
    """E se nunca houver duplicados?"""
    context["all_files"] = []
    return find_duplicate_files(context)


def _test_ignore_inexistent_files(context):
    """E se algum dos arquivos não existir?"""
    try:
        return find_duplicate_files(context)
    except ValueError:
        pass
