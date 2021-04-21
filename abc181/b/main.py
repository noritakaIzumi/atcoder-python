# -*- coding: utf-8 -*-

"""
"""


def main():
    n = int(input().strip())

    result = 0
    for _ in range(n):
        a, b = map(int, input().strip().split())
        result += (a + b) * (b - a + 1) // 2

    print(result)


if __name__ == '__main__':
    main()
