#  type: ignore
from abc import ABC
from math import ceil
from typing import Any, Generic, Optional, Sequence, TypeVar

from fastapi import Query
from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams
from fastapi_pagination.types import GreaterEqualOne
from pydantic import BaseModel

T = TypeVar("T")


class Params(BaseModel, AbstractParams):
    page_number: int = Query(1, ge=1, description="Page number")
    page_size: int = Query(10, ge=1, le=100, description="Page size")

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.page_size,
            offset=self.page_size * (self.page_number - 1),
        )


class BasePage(AbstractPage[T], Generic[T], ABC):
    data: Sequence[T]


class Page(BasePage[T], Generic[T]):
    page_size: Optional[GreaterEqualOne]
    is_last_page: bool

    __params_type__ = Params

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        params: AbstractParams,
        total: int,
        **kwargs: Any,
    ) -> T:
        if not isinstance(params, Params):
            raise ValueError("Page should be used with Params")

        pages = ceil(total / params.page_size) if total is not None else None
        is_last_page = params.page_number == pages

        return cls(
            data=items,
            page_size=params.page_size,
            is_last_page=is_last_page,
            **kwargs,
        )
