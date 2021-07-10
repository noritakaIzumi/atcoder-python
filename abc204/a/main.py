# -*- coding: utf-8 -*-

"""
"""


def main():
    x, y = map(int, input().strip().split())

    ans = x if x == y else 3 - x - y
    print(ans)


if __name__ == '__main__':
    main()
