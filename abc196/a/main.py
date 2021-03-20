# -*- coding: utf-8 -*-

# A - Difference Max

"""
整数 a, b, c, d がある。
a <= x <= b, c <= y <= d となるように整数 x, y を選ぶとき、x - y の最大値を求めよ。
"""


def main():
    a, b = map(int, input().strip().split())
    c, d = map(int, input().strip().split())
    # x を最大、y を最小とすればよい
    result = b - c
    print(result)


if __name__ == '__main__':
    main()
