# -*- coding: utf-8 -*-

"""
i 日目に i 円貯金
n 円以上になるのはいつか
"""


class Savings:
    def __init__(self):
        self.date = 0
        self.value = 0

    def save(self):
        self.date += 1
        self.value += self.date

    def is_more_than(self, n: int) -> bool:
        return self.value >= n


def main():
    n = int(input().strip())
    savings = Savings()

    while True:
        savings.save()
        if savings.is_more_than(n):
            break

    print(savings.date)


if __name__ == '__main__':
    main()
