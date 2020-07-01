from abc import ABC, abstractmethod


class FilesChainABC(ABC):
    @abstractmethod
    def do_files_process(self, read_from: str): pass
