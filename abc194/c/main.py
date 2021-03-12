# -*- coding: utf-8 -*-

# C - Squared Error

"""
長さ N の数列 A に対して、各要素同士の差の 2 乗の和を求める。
"""


def main():
    n = int(input())
    nums = list(map(int, input().strip().split()))

    result = 0
    result += sum(2 * n * nums[i] ** 2 for i in range(n))
    result -= 2 * sum(nums) ** 2
    result //= 2
    print(result)


if __name__ == '__main__':
    main()
