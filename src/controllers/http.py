import dataclasses

from fastapi import FastAPI, Path, Query
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from core.models.requests import BlocInfoRequest, SignaturesInfoRequest
from core.usecases.get_block_info import BlockInfo
from core.usecases.get_signature_info import SignatureInfo


def make_http_controller(
    block_info_usecase: BlockInfo, signature_info_usecase: SignatureInfo
) -> FastAPI:
    controller = FastAPI()

    @controller.exception_handler(ValueError)
    async def http_exception_handler(request: Request, exc: ValueError) -> JSONResponse:
        print(type(request))
        print(type(exc))
        return JSONResponse(status_code=400, content={"error": str(exc)})

    @controller.get("/")
    def health() -> Response:
        return Response("OK")

    @controller.get("/v1/blocks/{block_number}")
    def blocks(
        block_number: int = Path(description="The height of the block"),
    ) -> JSONResponse:
        block_info_request = BlocInfoRequest()
        block_info_request.block_number = block_number
        response = block_info_usecase(block_info_request)
        return JSONResponse(content=dataclasses.asdict(response))

    @controller.get("/v1/signatures/{signature}")
    def signatures(
        signature: str = Path(
            description="ETH function hex signature", example="0x0bb1e8a0"
        ),
        page_size: int = Query(default=10, description="Page size in range 1-10"),
        page_number: int = Query(default=1, description="Page number starting at 1"),
    ) -> JSONResponse:
        signature_info_request = SignaturesInfoRequest(signature)
        signature_info_request.page_size = page_size
        signature_info_request.page_number = page_number
        response = signature_info_usecase(signature_info_request)
        return JSONResponse(content=dataclasses.asdict(response))

    return controller
