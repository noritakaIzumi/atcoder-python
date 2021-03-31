# -*- coding: utf-8 -*-

# B - Training Camp

"""
メモ
"""
mod = 10 ** 9 + 7


def main():
    n = int(input().strip())

    power = 1
    for i in range(1, n + 1):
        power *= i
        power %= mod

    print(power)


if __name__ == '__main__':
    main()
