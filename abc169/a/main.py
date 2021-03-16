# -*- coding: utf-8 -*-

# A - Multiplication 1

"""
A * B を求める。
"""


def multiply(a: int, b: int) -> int:
    return a * b


def main():
    line = map(int, input().strip().split())
    print(multiply(*line))


if __name__ == '__main__':
    main()
