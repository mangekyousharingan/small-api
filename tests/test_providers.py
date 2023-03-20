from types import GeneratorType
from unittest.mock import MagicMock, patch

from fastapi import HTTPException
import pytest
import requests

from adapters.byte_4 import Byte4
from adapters.get_block import GetBlockIo


def test_get_block_provider():
    with patch.object(requests, "post") as mock_requests_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "some-fake-data"}
        mock_requests_post.return_value = mock_response

        node_provider = GetBlockIo(
            "https://fake-website-url.io/mainnet/", "fake-api-key"
        )
        node_provider_response = node_provider.get_block(12345)

        assert type(node_provider_response) is dict
        assert len(node_provider_response) == 1
        assert node_provider_response["data"] == "some-fake-data"


def test_get_block_provider_non_successful_response():
    with patch.object(requests, "post") as mock_requests_post:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_requests_post.return_value = mock_response

        node_provider = GetBlockIo(
            "https://fake-website-url.io/mainnet/", "fake-api-key"
        )

        with pytest.raises(HTTPException):
            node_provider.get_block(12345)


def test_4byte_provider():
    with patch.object(requests, "get") as mock_requests_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": "some-fake-data",
            "next": "fake-next-url",
        }
        mock_requests_get.return_value = mock_response

        signature_provider = Byte4("https://fake-website-url.io")
        signature_provider_response = signature_provider.get_signatures("signature")

        assert type(signature_provider_response) is GeneratorType

        assert next(signature_provider_response)
        assert next(signature_provider_response)

        assert mock_requests_get.call_count == 2


def test_signature_provider_non_successful_response():
    with patch.object(requests, "get") as mock_requests_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        signature_provider = Byte4("https://fake-website-url.io")

        with pytest.raises(HTTPException):
            for data in signature_provider.get_signatures("fake-sig"):
                assert data
