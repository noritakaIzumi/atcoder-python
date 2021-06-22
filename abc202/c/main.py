# -*- coding: utf-8 -*-

"""
"""


def main():
    n = int(input().strip())
    a = map(int, input().strip().split())
    b = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))

    b_counts = [0 for _ in range(n + 1)]
    for i in range(n):
        b_counts[b[c[i] - 1]] += 1

    ans = 0
    for p in a:
        ans += b_counts[p]

    print(ans)


if __name__ == '__main__':
    main()
