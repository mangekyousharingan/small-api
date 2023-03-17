from dataclasses import dataclass
import json

import requests

from ports.node_provider import NodeProvider


@dataclass
class GetBlockIo(NodeProvider):
    url: str
    api_key: str
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [],
        "id": "getblock.io",
    }

    def __post_init__(self) -> None:
        self._headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}

    def get_block(self, block_number: int) -> dict:
        self.payload["params"] = [hex(block_number), False]
        response = requests.post(
            self.url, headers=self._headers, data=json.dumps(self.payload)
        )
        self._validate_response(response)
        response_json = response.json()
        return response_json
