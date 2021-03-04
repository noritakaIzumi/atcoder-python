#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A - Very Very Primitive Game

"""
Takahashi と Aoki がゲームをする。
Takahashi は A 個のアメ、Aoki は B 個のアメを持っている。
C = 0 ならば Takahashi が先手、C = 1 ならば Aoki が先手で、以下の操作を交互に繰り返す。
・自分の持っているアメを 1 個食べる。
先に操作を行えなくなった方が負けとすると、どちらが勝つか。
"""


class Candy:
    def __init__(self, stock: int) -> None:
        self.stock = stock

    def eat(self) -> None:
        self.stock -= 1

    def has_candy(self) -> bool:
        return self.stock > 0


def main():
    line = list(map(int, input().strip().split()))
    takahashi = Candy(line[0])
    aoki = Candy(line[1])
    turn = line[2]
    if turn not in [0, 1]:
        raise ValueError
    winner = ''
    operations = [takahashi.eat, aoki.eat]
    while True:
        if turn == 0:
            if takahashi.has_candy():
                takahashi.eat()
                turn = 1
            else:
                winner = 'Aoki'
                break
        elif turn == 1:
            if aoki.has_candy():
                aoki.eat()
                turn = 0
            else:
                winner = 'Takahashi'
                break
    print(winner)


if __name__ == '__main__':
    main()
