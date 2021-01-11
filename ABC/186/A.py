# -*- coding: utf-8 -*-

# A - Brick

"""
トラックが 1 台ある。
このトラックには合計で N キログラムの荷物を載せることができる。
このトラックに 1 個 W キログラムのレンガを最大でいくつ載せることができるか？
"""


def getMaxBrickCount(n: int, w: int) -> int:
    """1 台のトラックにレンガを最大でいくつ載せることができるか返します。

    Args:
        n: トラックの最大積載量
        w: レンガ 1 個あたりの重さ

    Returns:
        int: 1 台のトラックにレンガを最大でいくつ載せることができるか

    """
    return n // w


def parseInput(line: str) -> list:
    return [int(i) for i in line.rstrip().split()]


def main(line: str) -> int:
    return getMaxBrickCount(*parseInput(line))


def test():
    assert main('10 3') == 3
    assert main('1000 1') == 1000


if __name__ == '__main__':
    print(main(input()))
    # test()
