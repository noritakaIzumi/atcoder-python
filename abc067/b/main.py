# -*- coding: utf-8 -*-

# B - Snake Toy

"""
長い方から K 本選ぶ
"""


def main():
    _, k = map(int, input().strip().split())
    lengths = sorted(map(int, input().strip().split()), reverse=True)

    print(sum(lengths[:k]))


if __name__ == '__main__':
    main()
