from dataclasses import dataclass
from typing import Callable

from core.models.requests import SignaturesInfoRequest
from core.models.responses import SignaturesInfoResponse
from ports.signatures_provider import SignaturesProvider


@dataclass
class SignatureInfo:
    provider_factory: Callable[[], SignaturesProvider]

    def __call__(self, request: SignaturesInfoRequest) -> SignaturesInfoResponse:
        signatures_provider = self.provider_factory()
        response_json = signatures_provider.get_signatures()
        signatures_info_response = SignaturesInfoResponse([{"name": "_loan"}], 1, True)
        return signatures_info_response
