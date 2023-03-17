from abc import ABC, abstractmethod
from dataclasses import dataclass

from ports.provider import Provider


@dataclass
class NodeProvider(Provider, ABC):
    @abstractmethod
    def get_block(self, block_num: int) -> dict:
        pass
