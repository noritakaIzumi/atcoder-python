# -*- coding: utf-8 -*-

# B - Gentle Pairs

"""
xy 平面上に n 個の点。
点 i と点 j を通る直線の傾きが -1 以上 1 以下であるような i < j の個数を求める。
"""
from typing import List


def get_tilt(p1: List[int], p2: List[int]) -> float:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def main():
    point_count = int(input())
    points = [[int(i) for i in input().strip().split()] for _ in range(point_count)]
    result = 0
    for i in range(point_count - 1):
        for j in range(i + 1, point_count):
            if -1 <= get_tilt(points[i], points[j]) <= 1:
                result += 1
    print(result)


if __name__ == '__main__':
    main()
