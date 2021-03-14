# -*- coding: utf-8 -*-

# A - ABC Preparation

"""
高橋君は、プログラミングコンテストを開くことにした。
コンテストを 1 回開くには、100 点問題、200 点問題、300 点問題、400 点問題が 1 問ずつ必要。
100, 200, 300, 400 点問題の案がそれぞれ A_1, A_2, A_3, A_4 問あるとき、コンテストを最大で何回開けるか？
同じ問題は 1 回までしか使えない。
"""


class Contest:
    def __init__(self, prob_100: int, prob_200: int, prob_300: int, prob_400: int) -> None:
        self.prob_100 = prob_100
        self.prob_200 = prob_200
        self.prob_300 = prob_300
        self.prob_400 = prob_400
        self.held_times = 0

    class NotHoldableError(AttributeError):
        pass

    def hold(self) -> None:
        if self.prob_100 > 0 and self.prob_200 > 0 and self.prob_300 > 0 and self.prob_400 > 0:
            self.prob_100 -= 1
            self.prob_200 -= 1
            self.prob_300 -= 1
            self.prob_400 -= 1
            self.held_times += 1
            return

        raise Contest.NotHoldableError


def main():
    line = map(int, input().strip().split())
    # print(min(line))

    contest = Contest(*line)
    try:
        while True:
            contest.hold()
    except Contest.NotHoldableError:
        print(contest.held_times)


if __name__ == '__main__':
    main()
