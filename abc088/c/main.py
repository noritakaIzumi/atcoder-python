# -*- coding: utf-8 -*-

# C - Takahashi's Information

"""
行または列同士の引き算をすると同じ値が 3 つ並ぶはずである。
(1 行目) - (2 行目) で a_1 - a_2 が 3 つ並ぶ。
"""


class Answer:
    yes = 'Yes'
    no = 'No'


def main():
    c = [list(map(int, input().strip().split())) for _ in range(3)]

    answer = Answer.yes
    for i in range(2):
        row_diff = [c[i][j] - c[i + 1][j] for j in range(3)]
        if min(row_diff) != max(row_diff):
            answer = Answer.no
            break
    if answer == Answer.yes:
        for j in range(2):
            row_diff = [c[i][j] - c[i][j + 1] for i in range(3)]
            if min(row_diff) != max(row_diff):
                answer = Answer.no
                break

    print(answer)


if __name__ == '__main__':
    main()
