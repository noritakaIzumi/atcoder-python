# -*- coding: utf-8 -*-

"""
"""


def main():
    n = int(input().strip())
    a = map(int, input().strip().split())
    b = map(int, input().strip().split())

    ans = max(0, min(b) - max(a) + 1)
    print(ans)


if __name__ == '__main__':
    main()
