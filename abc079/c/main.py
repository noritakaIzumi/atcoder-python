# -*- coding: utf-8 -*-

# C - Train Ticket

"""
メモ
"""
from enum import Enum
from typing import Tuple, List

targetSum = 7


class OperatorEnum(Enum):
    minus = '-'
    plus = '+'

    def calc(self, x: int, y: int):
        if self == OperatorEnum.minus:
            return x - y
        elif self == OperatorEnum.plus:
            return x + y


class TrainFee:
    def __init__(self, value: int) -> None:
        self.value = value
        self.formula = str(value)

    def __eq__(self, other):
        return self.value == other

    def operate(self, op: OperatorEnum, x: int) -> None:
        self.value = op.calc(self.value, x)
        self.formula += f'{op.value}{x}'

    def equals(self):
        self.formula += f'={self.value}'


def generate_search_pattern(dim: int) -> Tuple[List[OperatorEnum], ...]:
    if dim == 1:
        return [OperatorEnum.minus], [OperatorEnum.plus]
    return tuple(pattern + [op] for pattern in generate_search_pattern(dim - 1) for op in OperatorEnum)


def main():
    a, b, c, d = map(int, list(input().strip()))

    ans = ''
    for pattern in generate_search_pattern(3):
        s = TrainFee(a)
        for operator, x in zip(pattern, [b, c, d]):
            s.operate(operator, x)
        if s == targetSum:
            s.equals()
            ans = s.formula

    print(ans)


if __name__ == '__main__':
    main()
