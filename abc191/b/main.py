# -*- coding: utf-8 -*-

# B - Remove It

"""
長さ N の整数列 A と整数 X。
A から X と等しい要素をすべて取り除き、残った要素をそのままの順序で並べた数列 A' を出力せよ。
"""


def main():
    line = list(map(int, input().strip().split()))
    x = line[1]
    integers = list(map(int, input().strip().split()))
    alive_integers = []
    while len(integers) > 0:
        integer = integers.pop()
        if integer == x:
            pass
        else:
            alive_integers.append(str(integer))
    print(' '.join(alive_integers[::-1]))


if __name__ == '__main__':
    main()
