# -*- coding: utf-8 -*-

"""
N が 3 の倍数 <=> N の各桁の和が 3 の倍数
"""


def main():
    n = map(int, list(input().strip()))

    digit_count = 0
    digit_sum = 0
    mods = {i: 0 for i in range(3)}
    for digit in n:
        digit_count += 1
        digit_sum += digit
        mods[digit % 3] += 1

    digit_sum_mod = digit_sum % 3
    if digit_sum_mod == 0:
        ans = 0
    elif digit_sum_mod == 1:
        if mods[1] >= 1 and digit_count > 1:
            ans = 1
        elif mods[2] >= 2 and digit_count > 2:
            ans = 2
        else:
            ans = -1
    elif digit_sum_mod == 2:
        if mods[2] >= 1 and digit_count > 1:
            ans = 1
        elif mods[1] >= 2 and digit_count > 2:
            ans = 2
        else:
            ans = -1
    else:
        ans = -1

    print(ans)


if __name__ == '__main__':
    main()
