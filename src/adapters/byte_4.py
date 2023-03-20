from dataclasses import dataclass
from typing import Iterator

import requests

from ports.signatures_provider import SignaturesProvider


@dataclass
class Byte4(SignaturesProvider):
    url: str

    def get_signatures(self, hex_signature: str) -> Iterator[dict]:
        params = {"hex_signature": hex_signature}
        response = requests.get(self.url, params=params)
        self._validate_response(response)
        response_json = response.json()
        yield response_json

        # checking if there is any next values for given signature
        # as it might have multiple names.
        while url := response_json["next"]:
            response = requests.get(url)
            self._validate_response(response)
            response_json = response.json()
            yield response_json
