# -*- coding: utf-8 -*-

# C - Mandarin Orange

"""
N 枚の皿。i 番目の皿に A_i 個のみかんがある。
高橋君は l 番目から r 番目のすべての皿からみかんを x 個ずつ取って食べる。
(l, r, x) を適切に選ぶと、高橋君は最大で何個のみかんを食べられるか。
"""
from typing import List


class Orange:
    @staticmethod
    def is_valid_input(n: int, dishes: List[int]) -> bool:
        return n == len(dishes)

    def __init__(self, n: int, dishes: List[int]) -> None:
        if not Orange.is_valid_input(n, dishes):
            raise ValueError
        self.n = n
        self.dishes = dishes

    def get_max_orange_count(self) -> int:
        result = 0
        for i in range(self.n):
            x = self.dishes[i]
            for j in range(i, self.n):
                x = min(x, self.dishes[j])
                result = max(result, x * (j - i + 1))
        return result


def main():
    n = int(input().strip())
    dishes = list(map(int, input().strip().split()))
    orange = Orange(n, dishes)
    print(orange.get_max_orange_count())


if __name__ == '__main__':
    main()
