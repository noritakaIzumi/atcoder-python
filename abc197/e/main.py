# -*- coding: utf-8 -*-

# E - Traveler

"""
数直線上に N 個のボール (色付き)
"""
from typing import Dict, List


def main():
    n = int(input().strip())
    balls = [list(map(int, input().strip().split())) for _ in range(n)]

    colors: Dict[int, List[int]] = {}
    for ball in balls:
        if ball[1] not in colors.keys():
            colors[ball[1]] = []
        colors[ball[1]].append(ball[0])

    colors_keys = sorted(colors.keys())
    colors_count = len(colors_keys)
    left = [min(colors[colors_keys[i]]) for i in range(colors_count)]
    right = [max(colors[colors_keys[i]]) for i in range(colors_count)]

    dp = [[0 for _ in range(2)] for _ in range(n + 1)]

    dp[0][0] = abs(right[0]) + (right[0] - left[0])
    dp[0][1] = abs(left[0]) + (right[0] - left[0])

    for i in range(1, colors_count):
        # noinspection DuplicatedCode
        dp[i][0] = min(
            dp[i - 1][0] + abs(right[i] - left[i - 1]) + (right[i] - left[i]),
            dp[i - 1][1] + abs(right[i] - right[i - 1]) + (right[i] - left[i]),
        )
        # noinspection DuplicatedCode
        dp[i][1] = min(
            dp[i - 1][0] + abs(left[i] - left[i - 1]) + (right[i] - left[i]),
            dp[i - 1][1] + abs(left[i] - right[i - 1]) + (right[i] - left[i]),
        )

    ans = min(
        dp[colors_count - 1][0] + abs(left[colors_count - 1]),
        dp[colors_count - 1][1] + abs(right[colors_count - 1])
    )

    print(ans)


if __name__ == '__main__':
    main()
