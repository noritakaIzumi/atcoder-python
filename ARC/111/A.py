# -*- coding: utf-8 -*-

# A - Simple Math 2

"""
正の整数 N, M に対し、 10^N / M を超えない最大の整数を M で割ったあまりを求める。
"""


def get_remainder(n: int, m: int) -> int:
    return pow(10, n, m ** 2) // m % m


def main(line: str):
    nums = map(int, line.split())
    return get_remainder(*nums)


def test():
    assert main('1 2') == 1
    assert main('2 7') == 0
    assert main('1000000000000000000 9997') == 9015


if __name__ == '__main__':
    print(main(input().strip()))
    # test()
