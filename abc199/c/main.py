# -*- coding: utf-8 -*-

"""
"""
from typing import List


def main():
    n: int = int(input().strip())  # 文字列の長さの半分
    s: List[str] = list(input().strip())  # 文字列
    q: int = int(input().strip())  # クエリの数

    # クエリを処理する
    flipped = 0
    for _ in range(q):
        t: int  # mode
        a: int  # index
        b: int  # index
        t, a, b = map(int, input().strip().split())

        if t == 1:
            a_ = (a - 1 + n * flipped) % (2 * n)
            b_ = (b - 1 + n * flipped) % (2 * n)
            s[a_], s[b_] = s[b_], s[a_]
        elif t == 2:
            flipped += 1

    if flipped % 2 == 1:
        s = s[n:] + s[:n]

    print(''.join(s))


if __name__ == '__main__':
    main()
