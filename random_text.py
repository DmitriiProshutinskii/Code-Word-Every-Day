import random
from dataclasses import dataclass
from aiogram.types import ParseMode


@dataclass
class TipOfTheDay:
    title: str
    description: str
    parse_mode: ParseMode

    def __repr__(self):
        return (
            f'*{self.title}*\n\n{self.description}')

    @staticmethod
    def from_json(data: map):
        return TipOfTheDay(
            data["fields"]["Title"],
            data["fields"]["Description"],
            ParseMode.MARKDOWN_V2
        )


@dataclass
class ThirtyTips:
    def __init__(self, records: map):
        self.tips = []
        for record in records["records"]:
            self.tips.append(TipOfTheDay.from_json(record))

    def get_random_text(self):
        n = random.randint(0, len(self.tips)-1)
        return self.tips[n]