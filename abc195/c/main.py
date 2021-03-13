# -*- coding: utf-8 -*-

# C - Comma

"""
高橋君が 1 以上 N 以下の整数をカンマ付きで 1 度ずつ書くとき、カンマは合計で何回書かれるか？
"""
import math


def get_comma_count(n: int) -> int:
    digit = math.floor(math.log10(n)) + 1
    n_comma = (digit - 1) // 3

    result = n_comma * (n - 10 ** (n_comma * 3) + 1)  # 一番カンマが多くなる整数の個数
    for i in range(n_comma):
        result += i * 999 * 10 ** (i * 3)

    return result


def main():
    n = int(input().strip())
    print(get_comma_count(n))


if __name__ == '__main__':
    main()
