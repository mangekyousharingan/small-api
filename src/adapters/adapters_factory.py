from dataclasses import dataclass

from adapters.byte_4 import Byte4
from adapters.get_block import GetBlockIo
from ports.node_provider import NodeProvider
from ports.signatures_provider import SignaturesProvider


@dataclass
class AdaptersFactory:
    config: dict

    def node_provider(self) -> NodeProvider:
        node_provider_config = self.config["providers"]["node"]["getBlock"]
        return GetBlockIo(**node_provider_config)

    def signatures_provider(self) -> SignaturesProvider:
        signature_provider_config = self.config["providers"]["signatures"]["byte_4"]
        return Byte4(**signature_provider_config)
