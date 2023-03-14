from dataclasses import dataclass
from typing import Callable

from core.models.requests import BlocInfoRequest
from core.models.responses import BlockInfoResponse
from ports.node_provider import NodeProvider


@dataclass
class BlockInfo:
    provider_factory: Callable[[], NodeProvider]

    def __call__(self, request: BlocInfoRequest) -> BlockInfoResponse:
        node_provider = self.provider_factory()
        response_json = node_provider.get_block(request.block_number)
        result = response_json["result"]
        bloc_data_response = self._prepare_response(result)
        return bloc_data_response

    def _prepare_response(self, node_provider_response: dict) -> BlockInfoResponse:
        return BlockInfoResponse(
            gas_limit=node_provider_response["gasLimit"],
            gas_used=node_provider_response["gasUsed"],
            number=node_provider_response["number"],
            difficulty=node_provider_response["difficulty"],
            total_difficulty=node_provider_response["totalDifficulty"],
        )
