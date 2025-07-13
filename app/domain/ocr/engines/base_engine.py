from abc import ABC, abstractmethod


class BaseEngine(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def recognize(self, file_path: str):
        pass