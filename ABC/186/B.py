# -*- coding: utf-8 -*-

# B - Blocks on Grid

"""
縦 H マス、横 W マスのマス目がある。
上から i 行目、左から j 列目のマスにはブロックが A{i,j} 個ある。

どのマスにも同じ個数のブロックがある状態にするには、最小で何個のブロックを取り除けばよいか？

Examples:
    こんな状態だったら、一番少ないマスのところが 2 個なので、そこにあわせてブロックの多いマスからブロックを取り除けばよい。::

        2 2 3
        3 2 2
"""


def get_removed_block_count(rows: list) -> int:
    min_block_count = min([min(row) for row in rows])
    return sum(sum(block_count - min_block_count for block_count in row) for row in rows)


def main():
    h, w = [int(i) for i in input().rstrip().split()]
    rows = [[int(j) for j in input().rstrip().split()] for _ in range(h)]
    print(get_removed_block_count(rows))


def test():
    assert get_removed_block_count([
        [2, 2, 3],
        [3, 2, 2],
    ]) == 2
    assert get_removed_block_count([
        [99, 99, 99],
        [99, 0, 99],
        [99, 99, 99],
    ]) == 792


if __name__ == '__main__':
    main()
    # test()
