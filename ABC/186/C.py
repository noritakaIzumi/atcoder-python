# -*- coding: utf-8 -*-

# C - Unlucky 7

"""
7 が嫌いな人ありけり。
1 以上 N 以下の整数のうち、 10 進法で表しても 8 進法で表しても 7 を含まないような数はいくつあるか？

Examples:
    - 8 は 10 進数で 8 、 8 進数で 10 なので条件を満たす数にカウントされる。
    - 23 は 10 進数で 23 、 8 進数で 27 なので条件を満たす数にカウントされない。
    といった具合。
"""


def has_7_in_base(m: int, num: int) -> bool:
    """整数を m 進数に直したとき 7 を含む？

    Args:
        m: 変換したい進数
        num: 整数

    Returns:
        bool:

    """
    while num > 0:
        num, mod = divmod(num, m)
        if mod == 7:
            return True
    return False


def is_unlucky_7(num: int) -> int:
    if has_7_in_base(10, num) or has_7_in_base(8, num):
        return 0
    return 1


def solve(n: int) -> int:
    """1 以上 N 以下の整数のうち、 10 進法で表しても 8 進法で表しても 7 を含まないような数はいくつあるか

    Args:
        n: 整数。

    Returns:
        int:

    """
    return sum(is_unlucky_7(m) for m in range(1, n + 1))


def main():
    n = int(input())
    print(solve(n))


def test():
    assert solve(7) == 6
    assert solve(20) == 17
    assert solve(100000) == 30555


if __name__ == '__main__':
    main()
    # test()
