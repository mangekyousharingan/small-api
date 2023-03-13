from dataclasses import dataclass
import json

import requests

from ports.node import Node


@dataclass
class GetBlock(Node):
    _url: str = "https://eth.getblock.io/mainnet/"
    _api_key: str = "7203d8ab-29f8-46d1-b81a-4f1f0cea5b7a"
    _headers = {"x-api-key": _api_key, "Content-Type": "application/json"}
    _payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [1, True],
        "id": "getblock.io",
    }

    def get_block(self, block_num: int) -> dict:
        self._payload["params"] = [hex(block_num), False]
        response = requests.post(
            self._url, headers=self._headers, data=json.dumps(self._payload)
        )
        response_json = response.json()
        return response_json


gb = GetBlock()
print(gb.get_block(26803))
