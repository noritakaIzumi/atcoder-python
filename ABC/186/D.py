# -*- coding: utf-8 -*-

# D - Sum of difference
# 解ききれなかった

def get_sum_of_difference(nums: list) -> int:
    # result = 0
    nums = sorted(nums)
    nums_count = len(nums)
    # print(nums)

    # print(sum(num * (i + 1) for i, num in enumerate(nums)))
    # print(sum(num * (nums_count - i) for i, num in enumerate(nums)))
    # return sum(num * (i + 1) for i, num in enumerate(nums)) - sum(num * (nums_count - i) for i, num in enumerate(nums))
    return sum(num * (i * 2 + 1 - nums_count) for i, num in enumerate(nums))

    # for i in range(nums_count):
    #     result += sum(nums[i:]) - nums[i] * (nums_count - i)
    #     print(sum(nums[i:]))
    #     print(nums[i] * (nums_count - i - 1))

    # for i in range(nums_count):
    #     for j in range(i, nums_count):
    #         result += abs(nums[i] - nums[j])

    # return result


def main():
    _ = int(input())
    nums = [int(i) for i in input().rstrip().split()]
    print(get_sum_of_difference(nums))


def test():
    assert get_sum_of_difference([5, 1, 2]) == 8
    assert get_sum_of_difference([31, 41, 59, 26, 53]) == 176


if __name__ == '__main__':
    main()
    # test()
