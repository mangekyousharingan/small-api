from starlette.testclient import TestClient

from tests.conftest import vcr


@vcr.use_cassette()
def test_pagination_no_pagination(client: TestClient):
    response = client.get("/v1/signatures/0x28d095d2")
    response_json = response.json()
    assert len(response_json["data"]) == 3
    assert response_json["is_last_page"] is True


@vcr.use_cassette()
def test_pagination_paginate_page_size_and_number(client: TestClient):
    page_size = 2
    response = client.get(f"/v1/signatures/0x28d095d2?page_size={page_size}")
    response_json = response.json()

    assert len(response_json["data"]) == page_size
    assert response_json["is_last_page"] is False
