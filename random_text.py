import random
from dataclasses import dataclass
from typing import List

from aiogram.types import ParseMode


@dataclass
class TipOfTheDay:
    title: str
    description: str
    parse_mode: ParseMode

    def __repr__(self):
        return (
            f'*{self.title}*\n\n{self.description}')


@dataclass
class ThirtyTips:
    tips: List[TipOfTheDay]

    def __init__(self):
        self.tips = [
            TipOfTheDay(
                title='Чистая функция',
                description="""В языках программирования *чистая функция* — это функция, которая:
                
1\. является детерминированной;
2\. не обладает побочными эффектами\.
                
Наличия только одного из свойств недостаточно для того, чтобы функция была чистой\.
                """,
                parse_mode=ParseMode.MARKDOWN_V2,
            ),

            TipOfTheDay(
                title='Парадигмы языка',
                description="""Это совокупность идей и понятий, определяющих стиль написания компьютерных программ \(подход к программированию\)\. Это способ концептуализации, определяющий организацию вычислений и структурирование работы, выполняемой компьютером\.
            """,
                parse_mode=ParseMode.MARKDOWN_V2,
            ),
        ]


class RandomText:
    tip = ThirtyTips()

    def get_random_text(self):
        n = random.randint(0, len(self.tip.tips)-1)
        return self.tip.tips[n]
