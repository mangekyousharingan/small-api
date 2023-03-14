from dataclasses import dataclass, field


@dataclass
class BlocInfoRequest:
    _block_number: int = field(default_factory=int)

    @property
    def block_number(self) -> int:
        return self._block_number

    @block_number.setter
    def block_number(self, value: int) -> None:
        if not value > 0:
            raise ValueError("Block number must be greater than 0")
        self._block_number = value


@dataclass
class SignaturesDataRequest:
    signature: str
    _page_number: int = 1
    _page_size: int = 10

    @property
    def page_number(self) -> int:
        return self._page_number

    @page_number.setter
    def page_number(self, value: int) -> None:
        if not value > 0:
            raise ValueError(f"Page number must be greater than {value}")
        self._page_number = value

    @property
    def page_size(self) -> int:
        return self._page_size

    @page_size.setter
    def page_size(self, value: int) -> None:
        if value not in range(1, 11):
            raise ValueError("Page size must be in range 1-10")
        self.page_size = value
