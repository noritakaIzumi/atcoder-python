# -*- coding: utf-8 -*-

# B - Break Number

"""
もっとも 2 で割れる回数が多いのは 2 のべき乗
"""


def main():
    n = int(input().strip())

    ans = 1
    while True:
        ans *= 2
        if ans > n:
            ans //= 2
            break

    print(ans)


if __name__ == '__main__':
    main()
