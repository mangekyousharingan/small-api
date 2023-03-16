from dataclasses import dataclass, field

from fastapi.exceptions import RequestValidationError


@dataclass
class BlocInfoRequest:
    _block_number: int = field(default_factory=int)

    @property
    def block_number(self) -> int:
        return self._block_number

    @block_number.setter
    def block_number(self, value: int) -> None:
        if not value > 0:
            raise RequestValidationError("Block number must be greater than 0")
        self._block_number = value


@dataclass
class SignaturesInfoRequest:
    hex_signature: str
