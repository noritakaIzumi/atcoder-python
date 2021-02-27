# -*- coding: utf-8 -*-

# B - Alcoholic

"""
お酒を N 杯飲む。
i 番目に飲んだお酒は量が V_i ml、アルコール度数が P_i %
アルコール摂取量が X ml を「超えると」酔う。
何杯目のお酒を飲んでいる時に酔うか出力する。
全部飲んでも酔わないときは -1 を出力する。
"""


class Human:
    """人間。お酒を飲む人。

    Attributes:
        sum_alcohol (int): アルコールの蓄積量 (ml) の 100 倍。
        border_drunk (int): 酔うライン。これを「超えると」酔う。

    """

    def __init__(self, border_drunk: int) -> None:
        """Constructor.

        Args:
            border_drunk (int): 酔うライン。これを「超えると」酔う。
        """
        self.sum_alcohol = 0
        self.border_drunk = border_drunk * 100

    def drink(self, v: int, p: int) -> None:
        self.sum_alcohol += v * p

    def is_drunk(self) -> bool:
        return self.sum_alcohol > self.border_drunk


def main():
    line = list(map(int, input().strip().split()))
    drink_count = line[0]
    # noinspection SpellCheckingInspection
    takahashi = Human(line[1])
    for i in range(drink_count):
        line = list(map(int, input().strip().split()))
        takahashi.drink(line[0], line[1])
        if takahashi.is_drunk():
            result = i + 1
            break
    else:
        result = -1
    print(result)


if __name__ == '__main__':
    main()
