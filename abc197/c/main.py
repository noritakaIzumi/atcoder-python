# -*- coding: utf-8 -*-

# C - ORXOR

"""
メモ
"""
from typing import List
from itertools import combinations
from functools import reduce
from operator import or_


def get_answer(n: int, a: List[int]) -> int:
    if n == 1:
        return a[0]
    # noinspection SpellCheckingInspection
    xors = set()
    for i in range(n - 1):
        for v in combinations(range(n - 1), i):
            xor = 0
            pos = 0
            for p in v:
                xor ^= reduce(or_, a[pos:p + 1])
                pos = p + 1
            xor ^= reduce(or_, a[pos:n])
            xors.add(xor)
    return min(xors)


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    print(get_answer(n, a))


if __name__ == '__main__':
    main()
