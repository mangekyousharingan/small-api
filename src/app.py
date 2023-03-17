from dataclasses import dataclass, field

from fastapi import FastAPI
import uvicorn
import yaml

from adapters.adapters_factory import AdaptersFactory
from controllers.http import make_http_controller
from core.usecases.get_block_info import BlockInfo
from core.usecases.get_signature_info import SignatureInfo


@dataclass
class SmallApi:
    http_controller: FastAPI = field(init=False)
    config: dict = field(init=False)

    def load_config(self) -> None:
        with open("./config/config.yaml") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def set_up(self) -> None:
        print("Setting up...")
        adapters_factory = AdaptersFactory(self.config)

        block_info_usecase = BlockInfo(adapters_factory.node_provider)
        signature_info_usecase = SignatureInfo(adapters_factory.signatures_provider)

        self.http_controller = make_http_controller(
            block_info_usecase, signature_info_usecase
        )

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=8080, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()
