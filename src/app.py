from dataclasses import dataclass, field


import uvicorn
from fastapi import FastAPI

from src.controllers.http import make_http_controller


@dataclass
class SmallApi:
    http_controller: FastAPI = field(init=False)
    config: dict = field(init=False)

    def load_config(self) -> None:
        print("Loading config...")

    def set_up(self) -> None:
        print("Setting up...")
        self.http_controller = make_http_controller()

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=8080, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()
