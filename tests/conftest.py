# type: ignore
from fastapi import FastAPI
from pytest import fixture
from starlette.testclient import TestClient
import vcr
import yaml

from src.adapters.adapters_factory import AdaptersFactory
from src.controllers.http import make_http_controller
from src.core.usecases.get_block_info import BlockInfo
from src.core.usecases.get_signature_info import SignatureInfo

vcr = vcr.VCR(
    cassette_library_dir="../tests/cassettes", filter_headers=[("x-api-key", "XXXXXX")]
)


@fixture
def app() -> FastAPI:
    with open("../src/config/config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    adapters_factory = AdaptersFactory(config)

    block_info_usecase = BlockInfo(adapters_factory.node_provider)
    signatures_info_usecase = SignatureInfo(adapters_factory.signatures_provider)

    app = make_http_controller(block_info_usecase, signatures_info_usecase)
    return app


@fixture
def client(app: FastAPI):
    return TestClient(app)
