# -*- coding: utf-8 -*-

# A - Redundant Redundancy

"""
N: 整数
2, 3, ..., N のどれで割っても 1 余る N 以上 10^13 以下の整数を出力する
"""

import sys


def solve(num: int) -> int:
    """問題を解く。

    Args:
        num: N

    Returns:
        2, 3, ..., N のどれで割っても 1 余る N 以上 10^13 以下の整数

    Examples:
        (1, 2, ..., N の最小公倍数) + 1 はこの問題の答えになる。

    """
    try:
        if num < 2 or num > 30:
            raise ValueError
        return get_least_common_multiple(num) + 1
    except ValueError:
        print('数字の指定がおかしいです', file=sys.stderr)
    return 0


def get_least_common_multiple(num: int) -> int:
    result = 1
    cur1 = 2
    while cur1 <= num:
        x = cur1
        y = result
        cur2 = 2
        while x > 1:
            if x % cur2 == 0:
                x /= cur2
                if y % cur2 == 0:
                    y /= cur2
                    continue
                else:
                    result *= cur2
            cur2 += 1
        cur1 += 1
    return result


def verify_output(num: int) -> bool:
    redundancy = solve(num)
    if redundancy < num or redundancy > 10 ** 13:
        return False
    m = 2
    while m <= num:
        if redundancy % m != 1:
            return False
        m += 1
    else:
        return True


def test():
    assert verify_output(2), 'basic case'
    assert verify_output(3), 'case 1'
    assert verify_output(10), 'case 2'
    assert verify_output(16), 'case 3'
    assert verify_output(30), 'case 4'


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()
    # test()
