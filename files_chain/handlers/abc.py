from abc import ABC, abstractmethod


class HandlerABC(ABC):
    @staticmethod
    @abstractmethod
    def execute(file_name: str) -> str: pass

