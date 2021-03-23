# -*- coding: utf-8 -*-

# PracticeA - Welcome to AtCoder

"""
入力:
a
b c
s

出力: a + b + c, s を 1 行で
"""


def main():
    a = int(input().strip())
    b, c = map(int, input().strip().split())
    s = input().strip()

    print(f'{a + b + c} {s}')


if __name__ == '__main__':
    main()
