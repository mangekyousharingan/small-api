from dataclasses import dataclass
import json

import requests

from ports.node_provider import NodeProvider


@dataclass
class GetBlockIo(NodeProvider):
    _url: str = "https://eth.getblock.io/mainnet/"
    _api_key: str = "7203d8ab-29f8-46d1-b81a-4f1f0cea5b7a"
    _headers = {"x-api-key": _api_key, "Content-Type": "application/json"}
    _payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [],
        "id": "getblock.io",
    }

    def get_block(self, block_number: int) -> dict:
        self._payload["params"] = [hex(block_number), False]
        response = requests.post(
            self._url, headers=self._headers, data=json.dumps(self._payload)
        )
        response_json = response.json()
        return response_json
