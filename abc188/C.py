# -*- coding: utf-8 -*-

# C - ABC Tournament

"""
2^N 人の選手がトーナメントをする。
選手 i のレートは A_i (if i != j, A_i != A_j)
2 人の選手が対戦すると、必ずレートの高い方が勝つ。
準優勝する選手の番号を求める。
"""
from typing import List


def validate_member_count(count: int) -> None:
    while count % 2 == 0:
        count /= 2
    if count != 1:
        raise ValueError('トーナメントの人数が 2 のべき乗ではありません')


class Tournament:
    def __init__(self, ratings: List[int], count: int) -> None:
        validate_member_count(count)
        self.ratings = ratings
        self.count = count

    def __get_winner(self, p1: int, p2: int) -> int:
        """レーティングが高い方の選手の番号を返します。

        Args:
            p1: 参加者番号。
            p2: 参加者番号。

        Returns:
            レーティングが高い方の選手の番号を返します。

        """
        if self.ratings[p1] > self.ratings[p2]:
            return p1
        if self.ratings[p1] < self.ratings[p2]:
            return p2
        raise ValueError('レーティングが同じ人がいます')

    def __get_loser(self, p1: int, p2: int) -> int:
        if self.ratings[p1] > self.ratings[p2]:
            return p2
        if self.ratings[p1] < self.ratings[p2]:
            return p1
        raise ValueError('レーティングが同じ人がいます')

    def __get_tournament_winner(self, participants: List[int]) -> int:
        """完全二分木トーナメントの優勝者の番号を求める。

        配列のカウントが 2 のべき乗かどうか、配列とカウントが一致しているかどうかのバリデーションはここでは行わないので、
        あらかじめバリデートしておくこと。

        Args:
            participants (:obj:`list` of :obj:`int`): 参加者の番号。

        Returns:
            優勝者の番号。番号は 1 から始まる。

        Examples:
            ``members = [1, 4, 2, 5]`` の場合、``4`` となる。

        """
        if len(participants) == 1:
            return participants[0]
        if len(participants) == 2:
            return self.__get_winner(*participants)

        a = int(len(participants) / 2)
        return self.__get_tournament_winner(
            [
                self.__get_tournament_winner(participants[:a]),
                self.__get_tournament_winner(participants[a:])
            ]
        )

    def get_second_place(self) -> int:
        """準優勝者を求める。

        Returns:
            準優勝の選手の番号。

        """
        participants = [i for i in range(len(self.ratings))]
        a = int(len(participants) / 2)
        return self.__get_loser(
            self.__get_tournament_winner(participants[:a]),
            self.__get_tournament_winner(participants[a:])
        )


def main():
    n = int(input())
    ratings = list(map(int, input().rstrip().split()))
    tournament = Tournament(ratings, pow(2, n))
    print(tournament.get_second_place() + 1)


if __name__ == '__main__':
    main()
