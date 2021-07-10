# -*- coding: utf-8 -*-

"""
"""


def main():
    n = int(input().strip())
    t = list(map(int, input().strip().split()))

    s = sum(t) + 1
    dp = [[False for _ in range(s)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
        dp[i][t[i]] = True
    for i in range(1, n):
        for j in range(s):
            if dp[i - 1][j]:
                dp[i][j] = True
                dp[i][j + t[i]] = True

    ans = s // 2
    while True:
        if dp[n - 1][ans]:
            break
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
