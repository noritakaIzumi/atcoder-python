# -*- coding: utf-8 -*-

"""
"""


def main():
    a, b, c = input().strip().split()

    result = ''
    if a == b:
        result = c
    elif b == c:
        result = a
    elif c == a:
        result = b
    else:
        result = '0'

    print(result)


if __name__ == '__main__':
    main()
