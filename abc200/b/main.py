# -*- coding: utf-8 -*-

"""
"""


def main():
    n, k = map(int, input().strip().split())

    while k >= 1:
        if n % 200 == 0:
            n //= 200
        else:
            n *= 1000
            n += 200
        k -= 1

    print(n)


if __name__ == '__main__':
    main()
