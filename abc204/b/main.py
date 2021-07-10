# -*- coding: utf-8 -*-

"""
"""


def main():
    _ = int(input().strip())
    a = map(int, input().strip().split())

    nuts = sum(map(lambda x: max(0, x - 10), a))
    print(nuts)


if __name__ == '__main__':
    main()
