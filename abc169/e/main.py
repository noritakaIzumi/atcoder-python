# -*- coding: utf-8 -*-

# E - Count Median

"""
N 個の整数 X_1, X_2, ..., X_N があり、A_i <= X_i <= B_i である。
X_1, X_2, ..., X_N の中央値として考えられる値はいくつあるか。
"""
import statistics
from typing import List


class MedianRange:
    def __init__(self, minimum: int, maximum: int) -> None:
        self.minimum = minimum
        self.maximum = maximum


def get_median_candidate_count(n: int, int_ranges: List[List[int]]) -> int:
    median_range = MedianRange(
        minimum=statistics.median(int_ranges[i][0] for i in range(n)),
        maximum=statistics.median(int_ranges[j][1] for j in range(n)),
    )
    if n % 2 == 0:
        return int((median_range.maximum + 0.1) * 2 // 1) - int((median_range.minimum + 0.1) * 2 // 1) + 1
    else:
        return int(median_range.maximum) - int(median_range.minimum) + 1


def main():
    n = int(input().strip())
    int_ranges = [[int(i) for i in input().strip().split()] for _ in range(n)]
    print(get_median_candidate_count(n, int_ranges))


if __name__ == '__main__':
    main()
