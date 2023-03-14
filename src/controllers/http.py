import dataclasses

from fastapi import FastAPI
from starlette.responses import JSONResponse, Response

from core.models.requests import BlocInfoRequest
from core.usecases.get_block_info import BlockInfo


def make_http_controller(block_info_usecase: BlockInfo) -> FastAPI:
    controller = FastAPI()

    @controller.get("/")
    def health() -> Response:
        return Response("OK")

    @controller.get("/v1/blocks/{block_num}")
    def blocks(block_num: int) -> JSONResponse:
        block_info_request = BlocInfoRequest()
        block_info_request.block_number = block_num
        response = block_info_usecase(block_info_request)
        return JSONResponse(content=dataclasses.asdict(response))

    @controller.get("/v1/signatures/{signature}")
    def signatures(signature: str) -> Response:
        return Response(f"signatures: {signature}")

    return controller
