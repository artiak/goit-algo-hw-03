"""
Provides solution for recursive directory copying.
"""
import sys
from pathlib import Path
import shutil


def main():
    """
    Handles Command Line arguments and calls 'copy_dir'.
    """
    args: list = sys.argv

    args_len = len(args)
    if args_len < 2 or args_len > 3:
        print("Usage: python task_01.py <arg1> <arg2='dist'>")
        sys.exit(1)

    if args_len == 2:
        copy_dir(args[1])
        sys.exit(0)

    copy_dir(args[1], args[2])


def copy_dir(str_src_path: str, str_dst_path: str = 'dist') -> None:
    """
    Copies all files from 'str_src_path' to 'str_dst_path'
    grouping them by types in corresponding folders.
    """
    src_path: Path = Path(str_src_path)
    if not src_path.exists():
        print(f"The source directory {str_src_path} does not exist.\
              Terminating the programm.")

        return

    dst_path: Path

    try:
        dst_path = _to_path(str_dst_path)
    except OSError as e:
        print(f"An OS error occured: {e}. Terminating the programm.")

        return

    _do_copy_dir(src_path, dst_path)


def _to_path(str_path: str) -> Path:
    path: Path = Path(str_path)

    if not path.exists():
        path.mkdir()

    return path


def _do_copy_dir(src: Path, dst: Path) -> None:
    if src.is_file():
        file_name: str = src.name
        file_ext = file_name.split('.')[-1]

        ext_folder: Path = dst / file_ext

        if not ext_folder.exists():
            ext_folder.mkdir()

        shutil.copy(src, ext_folder)

        return

    for child in src.iterdir():
        _do_copy_dir(child, dst)


if __name__ == "__main__":
    main()
