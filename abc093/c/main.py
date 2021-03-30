# -*- coding: utf-8 -*-

# C - Same Integers

"""
2 つを選んで 1 増やす -> 1 つを選んで 1 減らす
1 減らすには 1 回の操作でいいが、1 だけ増やすには 2 回の操作 (2 増やす -> 1 減らす) が必要
どれに揃えるか
"""


def get_op_count(before: int, after: int) -> int:
    if after == before:
        return 0

    diff = after - before
    if diff < 0:
        return -diff
    if diff > 0:
        q, mod = divmod(diff, 2)
        return q + mod * 2
    return 0


def main():
    a, b, c = map(int, input().strip().split())

    ans = min(
        get_op_count(b, a) + get_op_count(c, a),  # a にそろえる場合
        get_op_count(a, b) + get_op_count(c, b),  # b にそろえる場合
        get_op_count(a, c) + get_op_count(b, c),  # c にそろえる場合
    )
    print(ans)


if __name__ == '__main__':
    main()
