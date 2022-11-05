import json
from algosdk import account
import click
from rich.console import Console
from rich.table import Table

from vanipy.query import Query
from vanipy.result import Result


@click.group(help="A tool for very superficial Algorand addresses.")
@click.pass_context
def vanipy(ctx):
    # ensure that ctx.obj exists and is a dict (in case `vanipy()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)


@vanipy.command(help="Generate a vanity address with a given prefix.")
@click.argument("prefix")
@click.option("--json", "json_", is_flag=True, help="Output as JSON.")
@click.pass_context
def prefix(ctx, prefix, json_):
    query = Query(q=prefix)
    if not query.is_valid():
        print("Invalid pattern. Please, specify a base32 prefix.")
        return 1

    vanity_pk, vanity_address = account.generate_account()

    while (not vanity_address.startswith(prefix)):
        vanity_pk, vanity_address = account.generate_account()

    result = Result(pk=vanity_pk, address=vanity_address)

    if json_:
        print(result.json())

        return 0

    table = Table(title="Loads of Vanity")

    table.add_column("Address", style="magenta")
    table.add_column("Private key",
                     justify="right",
                     style="cyan",
                     no_wrap=True)
    table.add_column("Mnemonic", justify="right", style="green")

    table.add_row(result.address, result.pk, result.mnemonic())

    console = Console()
    console.print(table)

    return 0


def main():
    vanipy(obj={})


if __name__ == "__main__":
    main()
