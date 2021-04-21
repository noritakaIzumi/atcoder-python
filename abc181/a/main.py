# -*- coding: utf-8 -*-

"""
"""


class Color:
    white = 'White'
    black = 'Black'


def main():
    n = int(input().strip())
    mod = n % 2
    if mod == 0:
        result = Color.white
    else:
        result = Color.black

    print(result)


if __name__ == '__main__':
    main()
