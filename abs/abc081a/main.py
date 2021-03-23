# -*- coding: utf-8 -*-

# ABC081A - Placing Marbles

"""
1, 2, 3 の番号が付いた 3 つのマスからなるマス目
マス i に s_i が書かれている。s_i = 0 or 1。
1 が書いてあるマス目にビー玉を置くけど、いくつ置くことになるか？
"""


def main():
    s = input().strip()
    print(s.count('1'))


if __name__ == '__main__':
    main()
