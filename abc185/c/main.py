# -*- coding: utf-8 -*-

# C - Duodecim Ferra

"""
長さ L の棒が東西方向に横たわっている。L は整数。
この棒を 11 箇所で切断して 12 本に分割するとき、分割後の各棒の長さが整数になるような切断の仕方は全部で何通りあるか。

Notes:
    L - 1 個の要素から 11 個を選ぶ組み合わせを求めればよい。
    (L - 1)! / (11! * (L - 12)!)
"""
from functools import reduce
from operator import mul


# noinspection SpellCheckingInspection
def combination(n: int, r: int) -> int:
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    l = int(input().strip())
    print(combination(l - 1, 11))


if __name__ == '__main__':
    main()
