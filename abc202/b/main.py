# -*- coding: utf-8 -*-

"""
0, 1, 6, 8, 9 からなる文字列を 180 度回転させてできるやつを求める。
9 -> 6
8 -> 8
6 -> 6
1 -> 1
0 -> 0
あと、文字列を逆順にする。
"""


def reverse_str(s: str) -> str:
    if s == '0':
        return '0'
    if s == '1':
        return '1'
    if s == '6':
        return '9'
    if s == '8':
        return '8'
    if s == '9':
        return '6'


def main():
    s = list(input().strip())
    ans = ''.join(reversed(list(map(reverse_str, s))))

    print(ans)


if __name__ == '__main__':
    main()
