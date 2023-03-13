from dataclasses import dataclass


@dataclass
class GetBlockResponse:
    gas_limit: int
    gas_used: int
    number: int
    difficulty: int
    total_difficulty: int


@dataclass
class SignaturesResponse:
    data: list[dict[str, str]]
    page_size: int
    is_last_page: bool
