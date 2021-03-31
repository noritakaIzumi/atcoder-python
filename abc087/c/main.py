# -*- coding: utf-8 -*-

# C - Candies

"""
右方向または下方向への移動なので、移動方法はどこで下方向に行くかの N 通り。
下方向に移動したときの列は 2 行分すべてのアメを回収できる。
その列より左側は 1 行目、その列より右側は 2 行目のアメを回収できる。
"""


def main():
    n = int(input().strip())

    candy_paths = [0 for _ in range(n)]

    # 1 列目
    row = list(map(int, input().strip().split()))
    for i, candy in enumerate(row):
        for j in range(i, n):
            candy_paths[j] += candy

    # 2 列目
    row = list(map(int, input().strip().split()))[::-1]
    for i, candy in enumerate(row):
        for j in range(n - i):
            candy_paths[j] += candy

    ans = max(candy_paths)
    print(ans)


if __name__ == '__main__':
    main()
