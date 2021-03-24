# -*- coding: utf-8 -*-

# B - 81

"""
N が九九の答えの中にあるか？
"""


class Result:
    yes = 'Yes'
    no = 'No'


def is_in_mul_table(n: int) -> bool:
    if n == 0:
        return False

    for i in range(1, 9 + 1):
        q, mod = divmod(n, i)
        if mod == 0 and 1 <= q <= 9:
            return True

    return False


def main():
    n = int(input().strip())
    print(Result.yes if is_in_mul_table(n) else Result.no)


if __name__ == '__main__':
    main()
