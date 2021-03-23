# -*- coding: utf-8 -*-

# C - ℕ Coloring

"""
整数 N。
以下の条件を満たす長さ N の正の整数の列 A_1, A_2, ..., A_N であって、数列に現れる値の最大値が最小になるものを一つ出力せよ。
・i が j の約数ならば A_i != A_j (1 <= i < j <= N)
"""


def main():
    n = int(input().strip())

    ans = []
    index = 0
    while 2 ** index <= n:
        ans.extend([str(index + 1) for _ in range(2 ** index)])
        index += 1
    ans = ans[:n]

    print(' '.join(ans))


if __name__ == '__main__':
    main()
