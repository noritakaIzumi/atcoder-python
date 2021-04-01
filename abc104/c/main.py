# -*- coding: utf-8 -*-

"""
"""
from typing import NewType


class Column:
    problem_count = 'problem_count'
    complete_bonus = 'complete_bonus'


ProblemCount = NewType('ProblemCount', int)
Point = NewType('Point', int)
Difficulty = NewType('Difficulty', int)


def calculate_point(a: Point, b: ProblemCount) -> Point:
    return Point(a * b)


def main():
    d: ProblemCount  # Number of difficulties of problems
    g: Point  # Goal of score
    d, g = map(int, input().strip().split())

    problems = []
    for _ in range(d):
        p: ProblemCount  # 難易度ごとの問題数
        c: Point  # Complete bonus point
        p, c = map(int, input().strip().split())
        problems.append(
            {
                Column.problem_count: p,
                Column.complete_bonus: c
            }
        )

    min_solved_count: ProblemCount = ProblemCount(1000)
    # 全部解く問題の種類を全探索
    for i in range(2 ** d):
        point_sum: Point = Point(0)
        solved_count: ProblemCount = ProblemCount(0)
        easiest_solved_difficulty: Difficulty = Difficulty(d)
        for j in range(d):
            allocation: Point = Point(100 * (d - j))
            if i >> j & 1:
                easiest_solved_difficulty = Difficulty(d - 1 - j)
                solved_count += problems[easiest_solved_difficulty][Column.problem_count]
                point_sum += calculate_point(allocation, problems[easiest_solved_difficulty][Column.problem_count])
                point_sum += problems[easiest_solved_difficulty][Column.complete_bonus]
        if point_sum >= g:
            min_solved_count = min(min_solved_count, solved_count)
        if point_sum < g and easiest_solved_difficulty > 0:
            easiest_solved_difficulty -= 1
            allocation = Point(100 * (easiest_solved_difficulty + 1))
            expected_solved_count = ((g - point_sum) + allocation - 1) // allocation
            if expected_solved_count < problems[easiest_solved_difficulty][Column.problem_count]:
                solved_count += expected_solved_count
                min_solved_count = min(min_solved_count, solved_count)

    print(min_solved_count)


if __name__ == '__main__':
    main()
