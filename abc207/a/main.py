# -*- coding: utf-8 -*-

"""
2 枚の合計の最大値 = 3 枚の合計 - 3 枚のうちの最小値
"""


def main():
    nums = list(map(int, input().strip().split()))

    ans = sum(nums) - min(nums)
    print(ans)


if __name__ == '__main__':
    main()
