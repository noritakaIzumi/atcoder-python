# -*- coding: utf-8 -*-

# A - Digits Sum

"""
メモ
"""


def main():
    n = int(input().strip())

    ans = 100
    for i in range(1, n // 2 + 1):
        a = i
        b = n - i
        digit_sum = sum(map(int, str(a))) + sum(map(int, str(b)))
        if digit_sum < ans:
            ans = digit_sum

    print(ans)


if __name__ == '__main__':
    main()
