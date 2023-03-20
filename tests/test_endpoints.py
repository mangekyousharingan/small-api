# type: ignore
from starlette.testclient import TestClient

from tests.conftest import vcr


def test_health(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "OK"


@vcr.use_cassette()
def test_get_block_info(client: TestClient):
    expected_output = {
        "gas_limit": 5000,
        "gas_used": 0,
        "number": 26803,
        "difficulty": 1118498710520,
        "total_difficulty": 17799983080356592,
    }
    response = client.get("/v1/blocks/26803")
    assert response.status_code == 200
    assert response.json() == expected_output


@vcr.use_cassette()
def test_signature_info(client: TestClient):
    expected_output = {
        "data": [{"name": "_resumePausableContract(address)"}],
        "page_size": 1,
        "is_last_page": True,
    }
    response = client.get("/v1/signatures/0x562b706c")
    assert response.status_code == 200
    assert response.json() == expected_output
