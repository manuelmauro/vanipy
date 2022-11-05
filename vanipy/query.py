from dataclasses import dataclass
import re


@dataclass
class Query():
    q: str

    def is_valid(self) -> bool:
        x = re.findall('[A-Z2-7]', self.q)

        return len(x) == len(self.q)
