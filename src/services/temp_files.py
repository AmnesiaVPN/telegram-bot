import contextlib

from config import ROOT_PATH

__all__ = ('deleting_temporary_config_file',)


@contextlib.contextmanager
def deleting_temporary_config_file(telegram_id: int, config_file_text: str) -> bytes:
    file_path = ROOT_PATH / f'{telegram_id}.conf'
    try:
        file_path.write_text(config_file_text)
        with open(file_path, 'rb') as file:
            yield file
    finally:
        file_path.unlink(missing_ok=True)
