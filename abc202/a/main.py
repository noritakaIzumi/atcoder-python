# -*- coding: utf-8 -*-

"""
"""


def back_eye(n: int) -> int:
    return 7 - n


def main():
    a, b, c = map(int, input().strip().split())
    ans = sum(map(back_eye, [a, b, c]))

    print(ans)


if __name__ == '__main__':
    main()
