# -*- coding: utf-8 -*-

# C - Attention

"""
メモ
"""


class Direction:
    east = 'E'
    west = 'W'


def main():
    n = int(input().strip())
    s = input().strip() + 'W'

    min_attention_count = s[1:].count(Direction.east)
    current_attention_count = s[1:].count(Direction.east)
    for i in range(1, n):
        current_attention_count += s[i - 1].count(Direction.west) - s[i].count(Direction.east)
        min_attention_count = min(min_attention_count, current_attention_count)

    print(min_attention_count)


if __name__ == '__main__':
    main()
