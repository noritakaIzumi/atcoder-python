# -*- coding: utf-8 -*-

"""
"""
from typing import List


def meat_time(n: int, t: List[int]) -> int:
    """肉を焼く最小の時間を取得する。

    Args:
        n (int): the number of meats.
        t (int): 各肉を焼くのにかかる時間。

    Returns:
        int:

    """
    if n == 1:
        return t[0]
    if n == 2:
        return max(t)

    min_time = 200
    for i in range(1, 2 ** n - 1):
        steamers = [0, 0]
        for j in range(n):
            if i >> j & 1:
                steamers[0] += t[j]
            else:
                steamers[1] += t[j]
        min_time = min(min_time, max(steamers))

    return min_time


def main():
    meat_count = int(input().strip())
    time_to_welldone = [int(input().strip()) for _ in range(meat_count)]

    ans = meat_time(meat_count, time_to_welldone)
    print(ans)


if __name__ == '__main__':
    main()
