# -*- coding: utf-8 -*-

# B - Multiplication 2

"""
N 個の整数 A_1, A_2, ..., A_N に対して A_1 * A_2 * ... * A_N を求めよ。
ただし、結果が 10^18 を超える場合は代わりに -1 を出力する。
"""
from typing import List


def multiply(nums: List[int]) -> int:
    if min(nums) == 0:
        return 0
    prod = 1
    for num in nums:
        prod *= num
        if prod > 10 ** 18:
            return -1
    return prod


def main():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(multiply(nums))


if __name__ == '__main__':
    main()
