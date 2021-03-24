# -*- coding: utf-8 -*-

# B - Digits

"""
整数 N を K 進数で表すと何桁か
"""


def main():
    n, k = map(int, input().strip().split())

    ans = 1
    while n >= k:
        ans += 1
        n //= k

    print(ans)


if __name__ == '__main__':
    main()
