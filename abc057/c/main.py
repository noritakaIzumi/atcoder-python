# -*- coding: utf-8 -*-

# C - Digits in Multiplication

"""
メモ
"""
n_max_digit = 11


def get_max_digit(a: int, b: int) -> int:
    return max(len(str(a)), len(str(b)))


def main():
    n = int(input().strip())

    ans = n_max_digit
    tmp = 1
    while tmp <= n ** 0.5:
        q, mod = divmod(n, tmp)
        f = get_max_digit(tmp, q)
        if mod == 0 and f < ans:
            ans = f
        tmp += 1

    print(ans)


if __name__ == '__main__':
    main()
