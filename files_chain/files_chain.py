from files_chain.abc import FilesChainABC
from .handlers import HandlerJSON, HandlerXML, HandlerCSV, HandlerTXT
from enum import Enum


class FileHandlers(Enum):
    txt = HandlerTXT
    json = HandlerJSON
    xml = HandlerXML
    csv = HandlerCSV


class FilesChain(FilesChainABC):
    def __init__(self):
        self._file_result_name = 'result.txt'
        self._result = ''
        self._handlers = FileHandlers

    def do_files_process(self, read_from: str):
        with open(read_from, 'r') as f:
            for line in f.read().splitlines():
                name, handler = self._get_handler(line)
                self._log(line, name)
                self._result += handler.execute(line)

        with open(self._file_result_name, 'w') as f:
            f.write(self._result)

    def _get_handler(self, file_path: str):
        ext = file_path.split('.')[-1]
        return self._handlers[ext].name, self._handlers[ext].value

    @staticmethod
    def _log(file_path, name):
        print(f'Обработчик "{name}" получил файл "{file_path}"')
