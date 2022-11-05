import click
from rich.console import Console

from vanipy.query import Query, QueryType
from vanipy.result import table_out, json_out
from vanipy.vanity import vanity_search


@click.group(help="A tool for very superficial Algorand addresses.")
@click.pass_context
def vanipy(ctx):
    # ensure that ctx.obj exists and is a dict (in case `vanipy()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)


@vanipy.command(help="Generate a vanity address with a given prefix.")
@click.argument("prefixes", nargs=-1)
@click.option("--json", "json_", is_flag=True, help="Output as JSON.")
@click.pass_context
def prefix(ctx, prefixes, json_):
    queries = []
    results = []
    for prefix in prefixes:
        query = Query(q=prefix, type_=QueryType.PREFIX)
        if not query.is_valid():
            print("Invalid pattern. Please, specify a base32 prefix.")
            return 1

        queries.append(query)

    for query in queries:
        results.append(vanity_search(query))

    if json_:
        out = json_out(results)
        print(out)
        return 0

    table = table_out(results)
    console = Console()
    console.print(table)
    return 0


@vanipy.command(help="Generate a vanity address satisfying a given regex.")
@click.argument("regexes", nargs=-1)
@click.option("--json", "json_", is_flag=True, help="Output as JSON.")
@click.pass_context
def regex(ctx, regexes, json_):
    queries = []
    results = []
    for regex in regexes:
        query = Query(q=regex, type_=QueryType.REGEX)

        if not query.is_valid():
            print("Invalid pattern. Please, specify a Python regex.")
            return 1

        queries.append(query)

    for query in queries:
        results.append(vanity_search(query))

    if json_:
        out = json_out(results)
        print(out)
        return 0

    table = table_out(results)
    console = Console()
    console.print(table)
    return 0


def main():
    vanipy(obj={})


if __name__ == "__main__":
    main()
