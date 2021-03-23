# -*- coding: utf-8 -*-

# A - RGB Cards

"""
4 * 25 = 100
"""


def main():
    r, g, b = map(int, input().strip().split())

    result = 'YES' if (g * 10 + b) % 4 == 0 else 'NO'
    print(result)


if __name__ == '__main__':
    main()
