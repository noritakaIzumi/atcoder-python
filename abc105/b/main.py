# -*- coding: utf-8 -*-

# B - Cakes and Donuts

"""
ケーキ: 4 ドル / 個
ドーナツ: 7 ドル / 個
合計 N ドルになる買い方あるか？

N を 4 で割ったあまりでドーナツの個数を 4 で割ったあまりが決まる
"""


class Result:
    yes = 'Yes'
    no = 'No'


def main():
    n = int(input().strip())

    result = Result.no
    mod = n % 4
    donuts = (4 - mod) % 4
    if n >= 7 * donuts and (n - donuts * 7) % 4 == 0:
        result = Result.yes

    print(result)


if __name__ == '__main__':
    main()
