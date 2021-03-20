# -*- coding: utf-8 -*-

# B - Round Down

"""
整数または小数 X が与えられるので、小数点以下を切り捨てて整数で出力せよ。
"""


def main():
    x = input().strip()
    pos_dot = x.find('.')
    if pos_dot >= 0:
        int_part = x[:pos_dot]
    else:
        int_part = x
    print(int_part)


if __name__ == '__main__':
    main()
