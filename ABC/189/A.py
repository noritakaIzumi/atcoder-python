# -*- coding: utf-8 -*-

# A - Slot

"""
スロットを回す。
結果：3 文字の英大文字で表され、これらがすべて同じ文字であるとき当たり。
当たりなら Won、はずれなら Lost を出力する。
"""


class SlotResult:
    won = 'Won'
    lost = 'Lost'


def slot_validation(chars: str) -> bool:
    if len(chars) != 3:
        return False
    return True


def is_win(chars: str) -> bool:
    for i in range(2):
        if chars[i] != chars[i + 1]:
            return False
    return True


def main():
    chars = input().strip()
    if slot_validation(chars) and is_win(chars):
        output = SlotResult.won
    else:
        output = SlotResult.lost
    print(output)


if __name__ == '__main__':
    main()
