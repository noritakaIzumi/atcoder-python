# -*- coding: utf-8 -*-

# B - Many 110

"""
S: 110 を 10^10 個連結した文字列
T: 長さ N の文字列 T (1 <= N <= 2 * 10^5)
T は 0, 1 からなる。

S に T が連続する部分文字列としていくつ含まれるかを求める。
"""


def solve(num: int, slug: str) -> int:
    """問題を解く。

    Args:
        num: N
        slug: T (部分文字列)

    Returns:
        S に slug が連続する部分文字列としていくつ含まれるか。

    Examples:
        110110110 に 1101 は 2 つ含まれる。

        - "1101"10110
        - 110"1101"10
    """

    try:
        if num < 1 or num > 2 * 10 ** 5:
            raise ValueError
        if len(slug) != num:
            raise ValueError
        return get_result(num, slug)
    except ValueError:
        print('引数が不正です')


def get_result(slug_length: int, slug: str) -> int:
    if slug_length == 1:
        if slug == '1':
            return 2 * 10 ** 10
        if slug == '0':
            return 10 ** 10
        return 0
    if slug_length == 2:
        if slug in ['11', '10']:
            return 10 ** 10
        if slug == '01':
            return 10 ** 10 - 1
        return 0
    if slug_length == 3:
        if slug == '110':
            return 10 ** 10
        if slug in ['101', '011']:
            return 10 ** 10 - 1
        return 0

    first_3chars = slug[:3]
    q, mod = divmod(slug_length, 3)
    if first_3chars == '110' and slug == first_3chars * q + slug[:mod]:
        return 10 ** 10 - (slug_length - 1) // 3
    if first_3chars == '101' and slug == first_3chars * q + slug[:mod]:
        return 10 ** 10 - q
    if first_3chars == '011' and slug == first_3chars * q + slug[:mod]:
        return 10 ** 10 - (slug_length + 1) // 3
    return 0


def test():
    assert solve(1, '1') == 20000000000, 'basic case 1'
    assert solve(1, '0') == 10000000000, 'basic case 2'
    assert solve(2, '11') == 10000000000, 'basic case 3'
    assert solve(2, '10') == 10000000000, 'basic case 4'
    assert solve(2, '01') == 9999999999, 'basic case 5'
    assert solve(3, '110') == 10000000000, 'basic case 6'
    assert solve(3, '101') == 9999999999, 'basic case 7'
    assert solve(3, '011') == 9999999999, 'basic case 8'
    assert solve(1, '2') == 0, 'error case 1'
    assert solve(2, '12') == 0, 'error case 2'
    assert solve(3, '012') == 0, 'error case 3'
    assert solve(4, '1011') == 9999999999, 'case 1'
    assert solve(22, '1011011011011011011011') == 9999999993, 'case 2'
    assert solve(4, '1101') == 9999999999, 'case 3'
    assert solve(5, '01101') == 9999999998, 'case 4'
    assert solve(6, '101101') == 9999999998, 'case 5'
    assert solve(24, '101101101101101101101101') == 9999999992, 'case 6'
    assert solve(4, '1102') == 0, 'error case 4'
    assert solve(4, '1012') == 0, 'error case 5'
    assert solve(4, '0112') == 0, 'error case 6'


def main():
    n = int(input())
    t = input()
    print(solve(n, t))


if __name__ == '__main__':
    main()
    # test()
