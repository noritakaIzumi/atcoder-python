# -*- coding: utf-8 -*-

# B - Quizzes

"""
N 問のクイズに答える。
持ち点は X 点で、正解すると 1 点増え、不正解だと 1 点減る。
ただし、持っている点数が 0 点の時に不正解となった場合は点数は減らない。

クイズの結果が文字列 S で与えられ、
左から i 番目の文字が "o" なら i 問目が正解、
"x" のとき i 問目が不正解だったことを表す。

最終的な点数を求める。
"""


class QuizResult:
    CORRECT = 'o'
    INCORRECT = 'x'


class Quiz:
    def __init__(self, quiz_count: int, points: int) -> None:
        self.quiz_count = quiz_count
        self.points = points

    def increase_points(self) -> None:
        self.points += 1

    def decrease_points(self) -> None:
        if self.points == 0:
            return
        self.points -= 1


def main():
    quiz_count, points = map(int, input().strip().split())
    quiz = Quiz(quiz_count, points)

    quiz_results = input().strip()
    for result in quiz_results:
        if result == QuizResult.CORRECT:
            quiz.increase_points()
        elif result == QuizResult.INCORRECT:
            quiz.decrease_points()

    print(quiz.points)


if __name__ == '__main__':
    main()
