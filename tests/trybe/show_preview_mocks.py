from pro_filer.entities import Context


"""
def show_preview(context_obj):
    print(
        f'Found {len(context_obj["all_files"])} files '
        f'and {len(context_obj["all_dirs"])} directories'
    )
    if context_obj["all_files"] or context_obj["all_dirs"]:
        print(f'First 5 files: {context_obj["all_files"][:5]}')
        print(f'First 5 directories: {context_obj["all_dirs"][:5]}')
"""


def _test_show_preview_only_with_empty_path(context: Context):
    """E se a função sempre considerar que o diretório está vazio?"""
    print("Found 0 files and 0 directories")


def _test_show_preview_does_not_slice_lists_before_printing(context: Context):
    """E se a função sempre mostrar todos os arquivos e diretórios?"""
    print(
        f'Found {len(context["all_files"])} files '
        f'and {len(context["all_dirs"])} directories'
    )
    if context["all_files"] or context["all_dirs"]:
        print(f'First 5 files: {context["all_files"]}')
        print(f'First 5 directories: {context["all_dirs"]}')
