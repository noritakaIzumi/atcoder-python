# -*- coding: utf-8 -*-

# A - Discount

"""
定価 A 円の商品が B 円で売られているとき、この商品の売値は定価の何パーセント引きか？

Notes:
    答えは小数
    想定解答との絶対誤差または相対誤差が 10^-2 以下であれば正解とみなされる。
"""


def main():
    line = list(map(int, input().strip().split()))
    result = (line[0] - line[1]) * 100 / line[0]
    print(result)


if __name__ == '__main__':
    main()
