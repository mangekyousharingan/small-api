from dataclasses import dataclass

import requests

from ports.signatures_provider import SignaturesProvider


@dataclass
class Byte4(SignaturesProvider):
    _url = "https://www.4byte.directory/api/v1/signatures/"
    _params = {}

    def get_signatures(
        self, hex_signature: str, page_size: int, page_number: int
    ) -> dict:
        self._params = {"hex_signature": hex_signature}
        response = requests.get(self._url, params=self._params)
        response_json = response.json()
        return response_json
