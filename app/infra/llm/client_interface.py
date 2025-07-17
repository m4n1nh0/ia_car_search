from abc import ABC, abstractmethod


class ClientInterface(ABC):
    @abstractmethod
    def extract_filters(self, user_input: str) -> dict:
        pass

    @abstractmethod
    def generate_response(self, context: dict) -> str:
        pass
