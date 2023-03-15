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
        response_json = signatures_provider.get_signatures(
            request.hex_signature, request.page_size, request.page_number
        )
        signatures_info_response = self._prepare_response(response_json)
        return signatures_info_response

    def _prepare_response(
        self, signatures_provider_response: dict
    ) -> SignaturesInfoResponse:
        #  TODO:  one signature might have multiple names, adjust for pagination
        results = signatures_provider_response["results"]
        signature_info_response = SignaturesInfoResponse(
            data=[{"name": data["text_signature"]} for data in results],
            page_size=signatures_provider_response["count"],
            is_last_page=True if not signatures_provider_response["next"] else False,
        )
        return signature_info_response
