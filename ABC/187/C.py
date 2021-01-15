# -*- coding: utf-8 -*-

# C - 1-SAT

"""
N 個の文字列 S_1, S_2, ..., S_N
各英小文字からなる空でない文字列の先頭に ! を 0 文字か 1 文字付加したもの。
文字列 T は T の先頭に ! を 0 文字付加しても 1 文字付加しても S_1, S_2, ..., S_N のどれかに一致するとき、不満な文字列であるという。
不満な文字列があるかどうか判定する。
"""


def main():
    n = int(input().strip())
    words = set(input().strip() for _ in range(n))
    for word in words:
        if '!' + word in words:
            print(word)
            break
    else:
        print('satisfiable')


if __name__ == '__main__':
    main()
