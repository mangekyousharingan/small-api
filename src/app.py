from dataclasses import dataclass, field

from fastapi import FastAPI
import uvicorn

from adapters.get_block import GetBlockIo
from controllers.http import make_http_controller
from core.usecases.get_block_info import BlockInfo


@dataclass
class SmallApi:
    http_controller: FastAPI = field(init=False)
    config: dict = field(init=False)

    def load_config(self) -> None:
        print("Loading config...")

    def set_up(self) -> None:
        print("Setting up...")

        block_info_usecase = BlockInfo(node_provider_factory)
        # signature_info_usecae = SignatureInfo(signature_provider_factory)

        self.http_controller = make_http_controller(block_info_usecase)

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=8080, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()


# TODO: temporary here, need to implement in better place
def node_provider_factory() -> GetBlockIo:
    return GetBlockIo()
