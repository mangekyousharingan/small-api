from dataclasses import dataclass, field
from typing import Optional

import uvicorn
from fastapi import FastAPI


@dataclass
class SmallApi:
    http_controller: Optional[FastAPI] = None
    config: dict = None

    def load_config(self) -> None:
        print("Loading config...")

    def set_up(self) -> None:
        print("Setting up...")

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=8080, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()
