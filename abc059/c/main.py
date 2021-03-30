# -*- coding: utf-8 -*-

# C - Sequence

"""
メモ
"""
from enum import auto, Enum


class ModeEnum(Enum):
    plus = auto()
    minus = auto()


class Operation:
    def __init__(self, nums_length: int, nums: list, mode: ModeEnum) -> None:
        self.nums_length = nums_length
        self.nums = nums
        self.mode = mode
        self.sum_ = 0
        self.op_count = 0

    def initialize(self) -> None:
        if self.mode == ModeEnum.plus:
            if self.nums[0] > 0:
                self.sum_ = self.nums[0]
            else:
                self.sum_ = 1
                self.op_count = -self.nums[0] + 1
        elif self.mode == ModeEnum.minus:
            if self.nums[0] < 0:
                self.sum_ = self.nums[0]
            else:
                self.sum_ = -1
                self.op_count = self.nums[0] + 1

    def operate(self) -> None:
        self.initialize()

        for i in range(1, self.nums_length):
            if self.sum_ * (self.sum_ + self.nums[i]) < 0:
                self.sum_ += self.nums[i]
            else:
                self.op_count += abs(self.sum_ + self.nums[i]) + 1
                self.sum_ = -self.sum_ // abs(self.sum_)


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    op1 = Operation(n, a, ModeEnum.plus)
    op1.operate()
    op2 = Operation(n, a, ModeEnum.minus)
    op2.operate()

    print(min(op1.op_count, op2.op_count))
    return


if __name__ == '__main__':
    main()
