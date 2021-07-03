# -*- coding: utf-8 -*-

"""
"""


class Travel:
    def __init__(self, money: int, friends: dict) -> None:
        self.money = money
        self.friends = friends
        self.current = 0

    def __move(self, target: int) -> None:
        move = min(self.money, target - self.current)
        self.money -= move
        self.current += move

    def move_to_next_friends(self, target: int) -> None:
        self.__move(target)
        if self.current == target:
            self.money += self.friends[target]


def main():
    n, money = map(int, input().strip().split())

    money_pos = []
    friends = {}
    for _ in range(n):
        a, b = map(int, input().strip().split())
        if not friends.get(a):
            friends[a] = 0
            money_pos.append(a)
        friends[a] += b

    money_pos.sort(reverse=True)
    travel = Travel(money, friends)
    while True:
        travel.move_to_next_friends(money_pos.pop())
        if travel.money <= 0:
            break
        if len(money_pos) <= 0:
            travel.current += travel.money
            break

    print(travel.current)


if __name__ == '__main__':
    main()
