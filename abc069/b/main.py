# -*- coding: utf-8 -*-

# B - i18n

"""
メモ
"""


def main():
    s = input().strip()
    result = s[0] + str(len(s) - 2) + s[-1]

    print(result)


if __name__ == '__main__':
    main()
