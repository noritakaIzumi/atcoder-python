# -*- coding: utf-8 -*-

# C - Doubled

"""
整数 N に対して、以下の条件を満たす 1 以上 N 以下の整数はいくつあるか？

・x の十進表記 (先頭に 0 を付けない) は偶数桁であり、その前半と後半は文字列として等しい
"""


def get_count(n: str) -> int:
    digit = len(n)
    if digit < 2:
        return 0
    if digit % 2 == 1:
        return get_count('9' * (digit - 1))
    half_digit = digit // 2
    first = int(n[:half_digit])
    last = int(n[half_digit:])

    result = first
    if first > last:
        result -= 1

    return result


def main():
    n = input().strip()
    print(get_count(n))


if __name__ == '__main__':
    main()
