# -*- coding: utf-8 -*-

"""
"""
import math


def main():
    r: int  # 1 回に移動可能な距離
    x: int  # x 座標
    y: int  # y 座標
    r, x, y = map(int, input().strip().split())

    dist = math.sqrt(x ** 2 + y ** 2)
    q = dist / r
    if q == 1:
        ans = 1
    elif q < 2:
        ans = 2
    else:
        ans = math.ceil(q)

    print(ans)


if __name__ == '__main__':
    main()
