# -*- coding: utf-8 -*-

# C - Kaprekar Number

"""
0 以上の整数 x に対して、
g_1(x) = x の各桁の数字を大きい順に並び変えてできる整数
g_2(x) = x の各桁の数字を小さい順に並び変えてできる整数
f(x) = g_1(x) - g_2(x)

整数 N, K に対し、a_0 = N, a_i+1 = f(a_i) (i > 0) で定まる数列の a_K を求める。
"""


# noinspection SpellCheckingInspection
def get_kaprekar_number(n: int) -> int:
    sorted_n = sorted(list(str(n)))
    g_2 = int(''.join(sorted_n))
    sorted_n.reverse()
    g_1 = int(''.join(sorted_n))
    return g_1 - g_2


def get_sequence_element(n: int, k: int) -> int:
    for _ in range(k):
        tmp = n
        n = get_kaprekar_number(n)
        if tmp == n:
            return n
    return n


def main():
    line = list(map(int, input().strip().split()))
    print(get_sequence_element(*line))


if __name__ == '__main__':
    main()
