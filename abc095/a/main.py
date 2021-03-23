# -*- coding: utf-8 -*-

# A - Something on It

"""
ラーメン 700 円
トッピング 1 つ 100 円

文字列 S の各文字が各トッピング乗せるかどうか (o で乗せる)
"""
RamenPrice = 700


class ToppingOrNot:
    yes = 'o'
    no = 'x'


def main():
    s = input().strip()
    topping_count = s.count(ToppingOrNot.yes)

    price = RamenPrice + 100 * topping_count
    print(price)


if __name__ == '__main__':
    main()
