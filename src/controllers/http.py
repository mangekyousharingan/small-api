import dataclasses

from fastapi import FastAPI
from starlette.responses import JSONResponse, Response

from core.models.requests import BlocInfoRequest, SignaturesInfoRequest
from core.usecases.get_block_info import BlockInfo
from core.usecases.get_signature_info import SignatureInfo


def make_http_controller(
    block_info_usecase: BlockInfo, signature_info_usecase: SignatureInfo
) -> FastAPI:

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
    def signatures(
        signature: str, page_size: int = 10, page_number: int = 1
    ) -> JSONResponse:
        signature_info_request = SignaturesInfoRequest(signature)
        signature_info_request.page_size = page_size
        signature_info_request.page_number = page_number
        response = signature_info_usecase(signature_info_request)
        return JSONResponse(content=dataclasses.asdict(response))

    return controller
