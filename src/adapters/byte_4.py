from dataclasses import dataclass

from ports.signatures_provider import SignaturesProvider


@dataclass
class Byte4(SignaturesProvider):
    def get_signatures(self) -> dict:
        print("Calling 4bytes....")
        return {}
