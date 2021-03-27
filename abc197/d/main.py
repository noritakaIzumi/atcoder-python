# -*- coding: utf-8 -*-

# D - Opposite

"""
正 N 角形 (N は偶数)
(x_0, y_0) と (x_N/2, y_N/2) の中点は正 N 角形の真ん中 (重心) となる。
"""
import math
from typing import List


def main():
    n: int  # 角の数
    n = int(input().strip())

    p_0: List[int]
    p_opposite: List[int]  # p_0 の反対側
    p_0 = list(map(int, input().strip().split()))
    p_opposite = list(map(int, input().strip().split()))

    center = [(p_0[i] + p_opposite[i]) / 2 for i in range(2)]
    segment_length = sum((p_0[i] - p_opposite[i]) ** 2 for i in range(2)) ** 0.5
    p_0_cos = (p_0[0] - p_opposite[0]) / segment_length
    p_0_sin = (p_0[1] - p_opposite[1]) / segment_length
    rad = 2 * math.pi / n
    rad_cos = math.cos(rad)
    rad_sin = math.sin(rad)
    p_1_cos = p_0_cos * rad_cos - p_0_sin * rad_sin
    p_1_sin = p_0_sin * rad_cos + p_0_cos * rad_sin
    p_1 = [segment_length / 2 * p_1_cos + center[0], segment_length / 2 * p_1_sin + center[1]]

    print(' '.join(map(str, p_1)))


if __name__ == '__main__':
    main()
