# -*- coding: utf-8 -*-

# B - Plus Matrix

"""
N 行 N 列の非負整数を成分とする行列 C がある。
すべての (i, j) について C_i,j = A_i + B_j を満たすような非負整数列 A_1, A_2, ..., A_N と B_1, B_2, ..., B_N の組が存在するか？
ある場合は一つ答えよ。
"""


def main():
    n = int(input().strip())
    a = []

    row_1 = list(map(int, input().strip().split()))
    for _ in range(n - 1):
        row_2 = list(map(int, input().strip().split()))
        diff = [row_2[i] - row_1[i] for i in range(n)]
        if min(diff) == max(diff):
            a.append(diff[0])
        else:
            result = ['No']
            break
    else:
        result = ['Yes']

        a = [0] + a
        if min(a) < 0:
            row_1 = list(map(lambda x: x + min(a), row_1))
            a = list(map(lambda x: x - min(a), a))

        result.append(' '.join(list(map(str, a))))
        result.append(' '.join(map(str, row_1)))

    print('\n'.join(result))


if __name__ == '__main__':
    main()
