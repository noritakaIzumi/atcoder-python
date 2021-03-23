# -*- coding: utf-8 -*-

# ABC088B - Card Game for Two

"""
Alice, Bob の順に、残っているカードのうち最大のものを取っていく
"""


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    a.sort(reverse=True)

    result = sum(a[i] * (-1) ** i for i in range(n))
    print(result)


if __name__ == '__main__':
    main()
