from fastapi import FastAPI
from starlette.responses import Response


def make_http_controller() -> FastAPI:
    controller = FastAPI()

    @controller.get("/")
    def health():
        return Response("OK")

    @controller.get("/v1/blocks/{block_num}")
    def blocks(block_num: int) -> Response:
        return Response("blocks")

    @controller.get("/v1/signatures/{signature}")
    def signatures(signature: str) -> Response:
        return Response("signatures")

    return controller
