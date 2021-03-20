# -*- coding: utf-8 -*-

# A - Determinant

"""
2 * 2 行列
[a, b]
[c, d]
の行列式を求める。
"""


def main():
    a, b = map(int, input().strip().split())
    c, d = map(int, input().strip().split())
    det = a * d - b * c
    print(det)


if __name__ == '__main__':
    main()
