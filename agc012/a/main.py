# -*- coding: utf-8 -*-

# A - AtCoder Group Contest

"""
パワー順に並び替えて、強い方から 2 人と弱い方から 1 人選んでチームを作ればよい
"""


def main():
    n = int(input().strip())
    a = sorted(map(int, input().strip().split()))

    print(sum(a[n::2]))


if __name__ == '__main__':
    main()
