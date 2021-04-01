# -*- coding: utf-8 -*-

"""
"""


def get_all_sum(nums: str) -> int:
    ans = 0
    for i in range(2 ** (len(nums) - 1)):
        tmp = ''
        for j in range(len(nums) - 1):
            if i >> j & 1:
                ans += int(nums[-j - 1] + tmp)
                tmp = ''
            else:
                tmp = nums[-j - 1] + tmp
        ans += int(nums[0] + tmp)

    return ans


def main():
    s = input().strip()
    print(get_all_sum(s))


if __name__ == '__main__':
    main()
