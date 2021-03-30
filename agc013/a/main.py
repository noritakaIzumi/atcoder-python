# -*- coding: utf-8 -*-

# A - Sorted Arrays

"""
メモ
"""


def solve(n: int, a: list) -> int:
    if n == 1:
        return 1
    result = 1
    mode = 0  # 増加: 1, 減少: -1
    i = 1
    while i < n:
        if a[i - 1] < a[i]:
            if mode < 0:
                result += 1
                mode = 0
            else:
                mode = 1
        elif a[i - 1] > a[i]:
            if mode > 0:
                result += 1
                mode = 0
            else:
                mode = -1
        i += 1

    return result


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    print(solve(n, a))


if __name__ == '__main__':
    main()
