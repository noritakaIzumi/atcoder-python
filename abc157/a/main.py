# -*- coding: utf-8 -*-

# A - Duplex Printing

"""
N ページ全面印刷。1 面に 1 ページ。
"""


def main():
    n = int(input().rstrip())
    print((n + 1) // 2)


if __name__ == '__main__':
    main()
