# -*- coding: utf-8 -*-

# C - Together

"""
メモ
"""


def main():
    _ = int(input().strip())

    a = map(int, input().strip().split())
    counts = [0 for _ in range(10 ** 5 + 2)]
    for i in a:
        counts[i - 1] += 1
        counts[i] += 1
        counts[i + 1] += 1

    ans = max(counts)
    print(ans)


if __name__ == '__main__':
    main()
