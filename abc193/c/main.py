# -*- coding: utf-8 -*-

# C - Unexpressed

"""
1 以上 N 以下の整数のうち、2 以上の整数 a, b を用いて a^b と表せないものはいくつあるか？
"""
import math


def main():
    n = int(input())
    rn = math.floor(n ** 0.5)
    unexpressed = {}
    for i in range(2, rn + 1):
        target = i * i
        if unexpressed.get(target):
            continue
        while target <= n:
            unexpressed[target] = True
            target *= i
    print(n - len(unexpressed))


if __name__ == '__main__':
    main()
