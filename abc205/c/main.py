# -*- coding: utf-8 -*-

"""
"""


class Result:
    lt = '<'
    gt = '>'
    eq = '='


def main():
    a, b, c = map(int, input().strip().split())

    if c & 1:  # c is odd
        if a < b:
            result = Result.lt
        elif a > b:
            result = Result.gt
        else:
            result = Result.eq
    else:
        abs_a = abs(a)
        abs_b = abs(b)
        if abs_a < abs_b:
            result = Result.lt
        elif abs_a > abs_b:
            result = Result.gt
        else:
            result = Result.eq

    print(result)


if __name__ == '__main__':
    main()
