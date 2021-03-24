# -*- coding: utf-8 -*-

# B - Good Distance

"""
メモ
"""


def main():
    n, d = map(int, input().strip().split())

    ans = 0
    x = []
    for i in range(n):
        x_i = list(map(int, input().strip().split()))
        for x_j in x:
            dist = sum((y - z) ** 2 for y, z in zip(x_i, x_j)) ** 0.5
            if dist % 1 == 0:
                ans += 1
        x.append(x_i)

    print(ans)


if __name__ == '__main__':
    main()
