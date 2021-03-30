# -*- coding: utf-8 -*-

# C - Write and Erase

"""
メモ
"""


def main():
    n = int(input().strip())

    nums = set()
    for _ in range(n):
        a = int(input().strip())
        if a in nums:
            nums.remove(a)
        else:
            nums.add(a)

    print(len(nums))


if __name__ == '__main__':
    main()
