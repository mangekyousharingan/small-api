from dataclasses import dataclass
from typing import Iterable

import requests

from ports.signatures_provider import SignaturesProvider


@dataclass
class Byte4(SignaturesProvider):
    _url: str = "https://www.4byte.directory/api/v1/signatures/"
    _params: dict = {}

    def get_signatures(self, hex_signature: str) -> Iterable[dict]:
        self._params = {"hex_signature": hex_signature}
        response = requests.get(self._url, params=self._params)
        response_json = response.json()
        yield response_json

        # checking if there is any next values for given signature
        # as it might have multiple names.
        while url := response_json["next"]:
            response = requests.get(url)
            response_json = response.json()
            yield response_json
