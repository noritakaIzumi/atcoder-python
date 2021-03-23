# -*- coding: utf-8 -*-

# A - Infinite Coins

"""
1 円玉 A 枚と 500 円玉たくさんで N 円払えるか？
"""


def main():
    n = int(input().strip())
    a = int(input().strip())

    if a >= n % 500:
        result = 'Yes'
    else:
        result = 'No'

    print(result)


if __name__ == '__main__':
    main()
