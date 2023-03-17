from abc import ABC

from fastapi import HTTPException
from requests import Response


class Provider(ABC):
    def _validate_response(self, response: Response) -> None:
        if response.status_code != 200:
            raise HTTPException(
                500,
                {
                    "message": f"Something went wrong when calling: {response.url}",
                    "error": response.text,
                },
            )
