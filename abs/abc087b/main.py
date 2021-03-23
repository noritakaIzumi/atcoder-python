# -*- coding: utf-8 -*-

# ABC087B - Coins

"""
メモ
"""


def main():
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    x = int(input().strip())

    result = 0
    for i in range(min(x // 500, a) + 1):
        p = x - 500 * i
        for j in range(min(p // 100, b) + 1):
            q = p - 100 * j
            if q // 50 <= c:
                result += 1

    print(result)


if __name__ == '__main__':
    main()
