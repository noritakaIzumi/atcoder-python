# -*- coding: utf-8 -*-

# A - Large Digits

"""
整数 n に対して n を十進法で表したときの各桁の和を S(n) とする。
2 つの整数 A, B に対して S(A), S(B) のうち大きい方を出力する。
"""


def add_digit(num: str) -> int:
    result = 0
    for d in num:
        result += int(d)
    return result


def main():
    a, b = input().strip().split()
    print(max(add_digit(a), add_digit(b)))


if __name__ == '__main__':
    main()
