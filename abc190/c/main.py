#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# C - Bowls and Dishes

"""
1, 2, ..., N の番号が付いた N 個の皿と、1, 2, ..., M の番号が付いた M 個の条件。
条件 i は皿 A_i, B_i の両方にボールが 1 個以上置かれているとき満たされる。
1, 2, ..., K の番号が付いた K 人の人がいて、人 i は皿 C_i か皿 D_i のどちらか一方にボールを置く。
満たされる条件の最大値はいくつか？
"""


def main():
    line = list(map(int, input().strip().split()))
    condition_count = line[1]
    conditions = [list(map(int, input().strip().split())) for _ in range(condition_count)]
    people_count = int(input())
    choices = [list(map(int, input().strip().split())) for _ in range(people_count)]

    result = 0
    for i in range(2 ** people_count):
        choice_index = ('{num:0' + str(people_count) + 'b}').format(num=i)
        balls = {}
        for j, c in enumerate(choice_index):
            balls[choices[j][int(c)]] = True
        balls = balls.keys()

        met_condition_count = 0
        for condition in conditions:
            if condition[0] in balls and condition[1] in balls:
                met_condition_count += 1
        if met_condition_count > result:
            result = met_condition_count

    print(result)


if __name__ == '__main__':
    main()
