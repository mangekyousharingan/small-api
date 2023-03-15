from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SignaturesProvider(ABC):
    @abstractmethod
    def get_signatures(
        self, hex_signature: str, page_size: int, page_number: int
    ) -> dict:
        pass
