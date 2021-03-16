# -*- coding: utf-8 -*-

# C - Multiplication 3

"""
A * B の小数点以下を切り捨て、整数で答えよ。
"""


def main():
    line = input().strip().split()
    print(int(line[0]) * int(line[1].replace('.', '')) // 100)


if __name__ == '__main__':
    main()
