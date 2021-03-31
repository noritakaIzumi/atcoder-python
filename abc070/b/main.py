# -*- coding: utf-8 -*-

# B - Two Switches

"""
メモ
"""


def main():
    a, b, c, d = map(int, input().strip().split())

    ans = max(min(b, d) - max(a, c), 0)
    print(ans)


if __name__ == '__main__':
    main()
