from dataclasses import dataclass
from typing import Callable

from core.models.requests import SignaturesInfoRequest
from core.models.responses import SignaturesInfoResponse
from ports.signatures_provider import SignaturesProvider


@dataclass
class SignatureInfo:
    provider_factory: Callable[[], SignaturesProvider]

    def __call__(self, request: SignaturesInfoRequest) -> list[SignaturesInfoResponse]:
        signatures_provider = self.provider_factory()
        signatures_info_response = []
        for response_json in signatures_provider.get_signatures(request.hex_signature):
            for signature_info in self._prepare_response(response_json):
                signatures_info_response.append(signature_info)

        return signatures_info_response

    def _prepare_response(
        self, signatures_provider_response: dict
    ) -> SignaturesInfoResponse:
        results = signatures_provider_response["results"]
        for siganture_info in results:
            yield SignaturesInfoResponse(name=siganture_info["text_signature"])
