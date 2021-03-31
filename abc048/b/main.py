# -*- coding: utf-8 -*-

# B - Between a and b ...

"""
b 以下で割り切れるものの個数から a 未満で割り切れるものの個数を引く。
"""


def main():
    a, b, x = map(int, input().strip().split())

    dividable_lte_b = b // x
    dividable_lt_a = (a - 1) // x
    ans = dividable_lte_b - dividable_lt_a
    print(ans)


if __name__ == '__main__':
    main()
