# -*- coding: utf-8 -*-

# C - Half and Half

"""
メモ
"""


def main():
    a, b, c, x, y = map(int, input().strip().split())

    price = 0
    # a, b を 1 枚ずつ用意する（a, b どちらかが目標に達するまで）
    if a + b < c * 2:
        price += (a + b) * min(x, y)
    else:
        price += c * (min(x, y) * 2)
    # 残りのピザ
    count = abs(x - y)  # 枚数
    single_price = a if x > y else b  # 単品で買う場合 1 枚当たりの値段
    if c * 2 < single_price:
        price += c * (count * 2)
    else:
        price += single_price * count

    print(price)


if __name__ == '__main__':
    main()
