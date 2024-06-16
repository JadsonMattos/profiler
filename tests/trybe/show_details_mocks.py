from datetime import date, datetime
import os
from pro_filer.entities import Context


"""
def show_details(context: Context):
    file_path = context["base_path"]
    file_name = file_path.split("/")[-1]

    if not path.exists(file_path):
        print(f"File '{file_name}' does not exist")
        return

    print(f"File name: {file_name}")
    print(f"File size in bytes: {path.getsize(file_path)}")
    print(f"File type: {'directory' if path.isdir(file_path) else 'file'}")

    _, file_extension = path.splitext(file_name)

    print(f"File extension: {file_extension or '[no extension]'}")

    py_mod_date = date.fromtimestamp(path.getmtime(file_path))

    print(f"Last modified date: {py_mod_date}")
    print(f"Permissions: {oct(stat(file_path).st_mode)[-3:]}")
"""


def _test_right_logic_but_wrong_messages(context: Context):
    """E se a mensagem impressa não estiver com a descrição correta?"""
    file_path = context["base_path"]
    file_name = file_path.split("/")[-1]

    if not os.path.exists(file_path):
        print(f"_ '{file_name}' _")
        return

    print(f"_: {file_name}")
    print(f"_: {os.path.getsize(file_path)}")
    print(f"_: {'directory' if os.path.isdir(file_path) else 'file'}")

    _, file_extension = os.path.splitext(file_name)

    print(f"_: {file_extension or '[no extension]'}")

    py_mod_date = date.fromtimestamp(os.path.getmtime(file_path))

    print(f"_: {py_mod_date}")


def _test_uses_date_time_instead_of_date(context: Context):
    """E se a data de criação for timestamp, mostrando também o horário?"""
    file_path = context["base_path"]
    file_name = file_path.split("/")[-1]

    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist")
        return

    print(f"File name: {file_name}")
    print(f"File size in bytes: {os.path.getsize(file_path)}")
    print(f"File type: {'directory' if os.path.isdir(file_path) else 'file'}")

    _, file_extension = os.path.splitext(file_name)

    print(f"File extension: {file_extension or '[no extension]'}")

    py_mod_date = datetime.fromtimestamp(os.path.getmtime(file_path))

    print(f"Last modified date: {py_mod_date}")


def _test_no_validation_for_file_existance(context: Context):
    """E se o arquivo não existir?"""
    file_path = context["base_path"]
    file_name = file_path.split("/")[-1]

    print(f"File name: {file_name}")
    print(f"File size in bytes: {os.path.getsize(file_path)}")
    print(f"File type: {'directory' if os.path.isdir(file_path) else 'file'}")

    _, file_extension = os.path.splitext(file_name)

    print(f"File extension: {file_extension or '[no extension]'}")

    py_mod_date = date.fromtimestamp(os.path.getmtime(file_path))

    print(f"Last modified date: {py_mod_date}")


def _test_default_message_for_file_without_extension(context: Context):
    """E se o arquivo não tiver extensão?"""
    file_path = context["base_path"]
    file_name = file_path.split("/")[-1]

    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist")
        return

    print(f"File name: {file_name}")
    print(f"File size in bytes: {os.path.getsize(file_path)}")
    print(f"File type: {'directory' if os.path.isdir(file_path) else 'file'}")

    _, file_extension = os.path.splitext(file_name)

    print(f"File extension: {file_extension}")

    py_mod_date = date.fromtimestamp(os.path.getmtime(file_path))

    print(f"Last modified date: {py_mod_date}")
