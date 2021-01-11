# -*- coding: utf-8 -*-

# A - Three-Point Shot

"""
バスケットボールの試合が行われており、得点は X 対 Y 。(X と Y は異なる)
現在劣勢であるチームが 3 ポイントシュートを決めて優勢に立つことはできるか？（同点でなく点数を上回る）
"""
from enum import Enum
from typing import Tuple


class BasketballTeam:
    """バスケットボールのチームのクラス。

    点数を加算したり、他のチームと比べて優勢かどうか判断したりします。

    """

    def __init__(self, score: int = 0):
        """Constructor.

        Args:
            score (int): 現在のスコアなど。

        """
        self.score = score

    def __get_point(self, score: int):
        self.score += score

    def hit_three_point_shot(self):
        self.__get_point(3)

    def is_superior(self, team: __init__) -> bool:
        return self.score > team.score


def get_inferior(team1: BasketballTeam, team2: BasketballTeam) -> Tuple[BasketballTeam, BasketballTeam]:
    """優勢か劣勢か判断してチームを入れ替えたり入れ替えなかったりします。

    Args:
        team1 (BasketballTeam): チーム。
        team2 (BasketballTeam): チーム。

    Returns:
        (優勢チーム、劣勢チーム) のタプル。

    Examples:
        以下の場合、team2 が team1 より優勢なら ``sup = team2, inf = team1`` となります。::

            sup, inf = get_inferior(team1, team2)

    """
    if team1.is_superior(team2):
        return team1, team2
    if team2.is_superior(team1):
        return team2, team1


class YesOrNoEnum(Enum):
    YES = 'Yes'
    NO = 'No'


def solve(line: str):
    teams = list(map(BasketballTeam, map(int, line.strip().split())))
    sup, inf = get_inferior(*teams)
    inf.hit_three_point_shot()
    return YesOrNoEnum.YES.value if inf.is_superior(sup) else YesOrNoEnum.NO.value


def main():
    line = input()
    print(solve(line))


def test():
    assert solve("""3 5
""") == ("""Yes
""").strip()
    assert solve("""16 2
""") == ("""No
""").strip()
    assert solve("""12 15
""") == ("""No
""").strip()


if __name__ == '__main__':
    main()
    # test()
