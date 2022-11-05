from algosdk import account

from vanipy.result import Result
from vanipy.query import Query


def vanity_search(query: Query) -> Result:
    vanity_pk, vanity_address = account.generate_account()
    while (not query.matched_by(vanity_address)):
        vanity_pk, vanity_address = account.generate_account()

    return Result(pk=vanity_pk, address=vanity_address)
