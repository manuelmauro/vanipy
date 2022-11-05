from algosdk import mnemonic
from dataclasses import dataclass
import json
from rich.table import Table


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

    def mnemonic(self) -> str:
        return mnemonic.from_private_key(self.pk)


def result_table(results: list[Result]) -> Table:
    table = Table(title="Loads of Vanity", show_lines=True)

    table.add_column("Address", style="magenta")
    table.add_column("Private key",
                     justify="right",
                     style="cyan",
                     no_wrap=True)
    table.add_column("Mnemonic", justify="right", style="green")

    for result in results:
        table.add_row(result.address, result.pk, result.mnemonic())

    return table
