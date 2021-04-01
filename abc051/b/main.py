# -*- coding: utf-8 -*-

"""
"""


def main():
    k, s = map(int, input().strip().split())

    pattern_count = 0
    # X のループ
    for x in range(k + 1):
        if s - x > 2 * k:
            continue
        if s - x < 0:
            break
        pattern_count += min(s - x, 2 * k - (s - x)) + 1

    print(pattern_count)


if __name__ == '__main__':
    main()
