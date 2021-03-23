# -*- coding: utf-8 -*-

# ABC083B - Some Sums

"""
1 から N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和
"""


def get_some_sums_1(n: int, a: int, b: int) -> int:
    result = 0
    for i in range(1, n + 1):
        if a <= sum(list(map(int, list(str(i))))) <= b:
            result += i
    return result


def get_some_sums_2(n: int, a: int, b: int, carry: int = 0) -> int:
    if n < 10:
        nums = [carry + i for i in range(max(a, 0), b + 1) if i <= n]
        return sum(nums)
    first_digit = int(str(n)[0])
    digit_num = len(str(n))
    return sum(
        get_some_sums_2(
            10 ** (digit_num - 1) - 1, a - i, b - i, carry + 10 ** (digit_num - 1) * i) for i in
        range(first_digit)
    ) + get_some_sums_2(
        int(str(n)[1:]), a - first_digit, b - first_digit, carry + 10 ** (digit_num - 1) * first_digit
    )


def main():
    n, a, b = map(int, input().strip().split())
    # print(get_some_sums_1(n, a, b))
    print(get_some_sums_2(n, a, b))


if __name__ == '__main__':
    main()
