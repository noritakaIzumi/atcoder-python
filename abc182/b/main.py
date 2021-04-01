# -*- coding: utf-8 -*-

"""
"""
import operator


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    max_gcd_degree = 0
    ans = 0
    for i in range(2, max(a) + 1)[::-1]:
        mods = list(map(operator.mod, a, (i for _ in range(n))))
        gcd_degree = mods.count(0)
        if gcd_degree > max_gcd_degree:
            max_gcd_degree = gcd_degree
            ans = i

    print(ans)


if __name__ == '__main__':
    main()
