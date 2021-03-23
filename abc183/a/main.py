# -*- coding: utf-8 -*-

# A - ReLU

"""
メモ。
"""


def re_lu(x: int) -> int:
    if x < 0:
        return 0
    return x


def main():
    x = int(input().strip())
    print(re_lu(x))


if __name__ == '__main__':
    main()
