from typing import Any

from fastapi import FastAPI, Path
from fastapi_pagination import add_pagination, paginate
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from core.models.pagination import Page
from core.models.requests import BlocInfoRequest, SignaturesInfoRequest
from core.models.responses import BlockInfoResponse, SignaturesInfoResponse
from core.usecases.get_block_info import BlockInfo
from core.usecases.get_signature_info import SignatureInfo


def make_http_controller(
    block_info_usecase: BlockInfo, signature_info_usecase: SignatureInfo
) -> FastAPI:
    controller = FastAPI()

    @controller.exception_handler(Exception)
    async def http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content={"message": "Something went wrong!", "error": str(exc)},
        )

    @controller.get("/")
    def health() -> Response:
        return Response("OK")

    @controller.get("/v1/blocks/{block_number}", response_model=BlockInfoResponse)
    def blocks(
        block_number: int = Path(description="The height of the block"),
    ) -> Any:
        block_info_request = BlocInfoRequest()
        block_info_request.block_number = block_number
        response = block_info_usecase(block_info_request)
        return response

    @controller.get(
        "/v1/signatures/{signature}",
        response_model=Page[SignaturesInfoResponse]
        # TODO: reorganize Page to custom to get proper output.
    )
    def signatures(
        signature: str = Path(
            description="ETH function hex signature", example="0x0bb1e8a0"
        )
    ) -> Any:
        signature_info_request = SignaturesInfoRequest(signature)
        response = signature_info_usecase(signature_info_request)
        return paginate(response)

    add_pagination(controller)

    return controller
