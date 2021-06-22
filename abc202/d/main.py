# -*- coding: utf-8 -*-

"""
"""
from functools import reduce
from operator import mul


def collection(n: int, m: int) -> int:
    m = min(m, n - m)
    num = reduce(mul, range(n - m + 1, n + 1), 1)
    den = reduce(mul, range(1, m + 1), 1)
    return num // den


def main():
    a, b, k = map(int, input().strip().split())

    ans = ''
    while a > 0 and b > 0:
        x = collection(a + b - 1, a - 1)
        if x < k:
            ans += 'b'
            b -= 1
            k -= x
        else:
            ans += 'a'
            a -= 1
    ans += 'a' * a
    ans += 'b' * b

    print(ans)


if __name__ == '__main__':
    main()
