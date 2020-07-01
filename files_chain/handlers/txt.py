from .abc import HandlerABC


class HandlerTXT(HandlerABC):
    @staticmethod
    def execute(file_name: str) -> str:
        with open(file_name, 'r') as f:
            return f.read()
