from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class NodeProvider(ABC):
    @abstractmethod
    def get_block(self, block_num: int) -> dict:
        pass
