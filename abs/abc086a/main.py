# -*- coding: utf-8 -*-

# ABC086A - Product

"""
a と b の積が偶数か奇数か？
"""


def main():
    a, b = map(int, input().strip().split())
    result = 'Odd' if a & b & 1 else 'Even'

    print(result)


if __name__ == '__main__':
    main()
