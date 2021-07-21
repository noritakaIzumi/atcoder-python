# -*- coding: utf-8 -*-

"""
"""
import math


def main():
    a, b, c, d = map(int, input().strip().split())

    ans = -1
    # B が C の D 倍未満でなければ目標達成不可能
    if b >= c * d:
        pass
    else:
        # B < C * D
        # A + B * x <= C * x * D となる最小の x (回数)
        ans = math.ceil(a / (c * d - b))

    print(ans)


if __name__ == '__main__':
    main()
