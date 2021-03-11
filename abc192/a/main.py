# -*- coding: utf-8 -*-

# A - Star

"""
ゲームで、集めたコインが 100 の倍数になるごとにご褒美がもらえる。
今まで集めたコインが X 枚とすると、次のご褒美をもらうためにはコインを何枚集めればよいか？
"""


def main():
    line = int(input().strip())
    result = 100 - line % 100
    print(result)


if __name__ == '__main__':
    main()
