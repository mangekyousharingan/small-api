from dataclasses import dataclass, field

from fastapi import FastAPI
import uvicorn

from adapters.byte_4 import Byte4
from adapters.get_block import GetBlockIo
from controllers.http import make_http_controller
from core.usecases.get_block_info import BlockInfo
from core.usecases.get_signature_info import SignatureInfo
from ports.signatures_provider import SignaturesProvider


@dataclass
class SmallApi:
    http_controller: FastAPI = field(init=False)
    config: dict = field(init=False)

    def load_config(self) -> None:
        print("Loading config...")

    def set_up(self) -> None:
        print("Setting up...")

        block_info_usecase = BlockInfo(node_provider_factory)
        signature_info_usecase = SignatureInfo(signature_provider_factory)

        self.http_controller = make_http_controller(
            block_info_usecase, signature_info_usecase
        )

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=8080, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()


# TODO: temporary here, need to implement in better place
# For now both are simplified as we have only one provider for each
# when having more providers, more logic might be added here.
def node_provider_factory() -> GetBlockIo:
    return GetBlockIo()


def signature_provider_factory() -> SignaturesProvider:
    return Byte4()
