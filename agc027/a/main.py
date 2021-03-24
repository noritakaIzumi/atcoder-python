# -*- coding: utf-8 -*-

# A - Candy Distribution Again

"""
a_i が小さい順にお菓子あげれば喜ぶ人最大化可能
余計に配ると不満になる（最後の人のとき注意）
"""


def main():
    n: int
    x: int
    n, x = map(int, input().strip().split())

    a = sorted(map(int, input().strip().split()))
    sweets_sum = 0
    happy_children = 0
    for a_i in a:
        if a_i > x - sweets_sum:
            break
        sweets_sum += a_i
        happy_children += 1
    # すべての子に配り終えて、かつお菓子が余っているとき、最後の子にお菓子を余計に配って不満にさせるしかない
    else:
        if sweets_sum != x:
            happy_children -= 1

    print(happy_children)


if __name__ == '__main__':
    main()
