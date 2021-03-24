# -*- coding: utf-8 -*-

# B - Palindromic Numbers

"""
数字はすべて 5 桁
"""


def palindrome_count(a: int, b: int) -> int:
    x = a // 1000
    y = b // 1000

    result = 0
    if x == y:
        for i in range(10):
            if a <= int(str(x) + str(i) + str(x)[::-1]) <= b:
                result += 1
    else:
        result += palindrome_count(a, int(f'{str(x)}999'))
        result += 10 * len(range(x + 1, y))
        result += palindrome_count(int(f'{str(y)}000'), b)
    return result


def main():
    a, b = map(int, input().strip().split())
    print(palindrome_count(a, b))


if __name__ == '__main__':
    main()
