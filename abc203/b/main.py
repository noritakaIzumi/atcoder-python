# -*- coding: utf-8 -*-

"""
"""


def main():
    n, k = map(int, input().strip().split())

    ans = (1 + n) * n // 2 * 100 * k
    ans += (1 + k) * k // 2 * n
    print(ans)


if __name__ == '__main__':
    main()
