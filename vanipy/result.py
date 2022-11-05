from algosdk import mnemonic
from dataclasses import dataclass
import json


@dataclass
class Result():
    pk: str
    address: str

    def dictify(self) -> dict:
        return {
            "pk": self.pk,
            "addr": self.address,
            "mnemonic": self.mnemonic(),
        }

    def json(self) -> str:
        return json.dumps(self.dictify())

    def mnemonic(self) -> str:
        return mnemonic.from_private_key(self.pk)