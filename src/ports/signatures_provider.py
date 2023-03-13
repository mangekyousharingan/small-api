from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Signatures(ABC):
    @abstractmethod
    def get_signatures(self) -> dict:
        pass
