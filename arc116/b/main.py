# -*- coding: utf-8 -*-

# B - Products of Min-Max

"""
メモ
"""
q = 998244353


def main():
    n = int(input().strip())
    a = sorted(map(int, input().strip().split()))

    ans = pow(a[0], 2, q)
    mul = 0
    for i in range(1, n):
        mul = mul * 2 + a[i - 1]
        mul %= q
        ans += a[i] * (a[i] + mul)
        ans %= q

    print(ans)


if __name__ == '__main__':
    main()
