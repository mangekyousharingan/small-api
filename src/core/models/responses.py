from pydantic import BaseModel


class BlockInfoResponse(BaseModel):
    gas_limit: int
    gas_used: int
    number: int
    difficulty: int
    total_difficulty: int


class SignaturesInfoResponse(BaseModel):
    name: str
