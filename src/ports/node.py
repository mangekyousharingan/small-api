from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Node(ABC):

    @abstractmethod
    def get_block(self):
        pass
