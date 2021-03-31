# -*- coding: utf-8 -*-

# B - AtCoDeerくんとボール色塗り

"""
隣のボールを塗る色のパターンは K - 1 通り。
"""


def main():
    n, k = map(int, input().strip().split())

    ans = k * (k - 1) ** (n - 1)
    print(ans)


if __name__ == '__main__':
    main()
