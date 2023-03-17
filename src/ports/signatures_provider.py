from abc import ABC, abstractmethod
from dataclasses import dataclass

from ports.provider import Provider


@dataclass
class SignaturesProvider(Provider, ABC):
    @abstractmethod
    def get_signatures(self, hex_signature: str) -> dict:
        pass
