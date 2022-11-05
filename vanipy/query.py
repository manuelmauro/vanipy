from dataclasses import dataclass
from enum import Enum
import re


class QueryType(Enum):
    PREFIX = 0,
    REGEX = 1


@dataclass
class Query():
    type_: QueryType
    q: str

    def is_valid(self) -> bool:
        if self.type_ is QueryType.PREFIX:
            x = re.findall('[A-Z2-7]', self.q)
            return len(x) == len(self.q)
        elif self.type_ is QueryType.REGEX:
            # TODO unimplemented!
            return True

        return False

    def matched_by(self, address: str) -> bool:
        if self.type_ is QueryType.PREFIX:
            if address.startswith(self.q):
                return True
        elif self.type_ is QueryType.REGEX:
            # TODO find a graceful way to compile the regex once (i.e., use re.compile)
            if re.search(self.q, address) is not None:
                return True

        return False
