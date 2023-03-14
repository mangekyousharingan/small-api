from dataclasses import dataclass


@dataclass
class BlockInfoResponse:
    gas_limit: int
    gas_used: int
    number: int
    difficulty: int
    total_difficulty: int

    def __init__(
        self,
        gas_limit: str,
        gas_used: str,
        number: str,
        difficulty: str,
        total_difficulty: str,
    ):
        self.gas_limit: int = self._convert(gas_limit)
        self.gas_used: int = self._convert(gas_used)
        self.number: int = self._convert(number)
        self.difficulty: int = self._convert(difficulty)
        self.total_difficulty: int = self._convert(total_difficulty)

    def _convert(self, value: str) -> int:
        return int(value, 16)


@dataclass
class SignaturesResponse:
    data: list[dict[str, str]]
    page_size: int
    is_last_page: bool
