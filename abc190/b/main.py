#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# B - Magic 3

"""
高橋君は魔物と戦っている。
N 種類の呪文を使うことができる。
i 番目の呪文は詠唱に X_i 秒かかり、威力は Y_i。
魔物は強いので、詠唱に S 秒以上かかる呪文や、威力が D 以下の呪文ではダメージを与えられない。
また、呪文以外の方法でダメージを与えることもできない。
高橋君は魔物にダメージを与えらえれるか？
"""


class Monster:
    def __init__(self, time_limit: int, power_border: int) -> None:
        self.time_limit = time_limit
        self.power_border = power_border

    def receive_damage(self, time: int, power: int) -> bool:
        return time < self.time_limit and power > self.power_border


def main():
    line = list(map(int, input().strip().split()))
    monster = Monster(line[1], line[2])
    damageable = False
    for _ in range(line[0]):
        tech = list(map(int, input().strip().split()))
        if monster.receive_damage(*tech):
            damageable = True
            break
    print('Yes' if damageable else 'No')


if __name__ == '__main__':
    main()
