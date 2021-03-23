# -*- coding: utf-8 -*-

# A - Already 2018

"""
日付 S (yyyy/mm/dd) を 2017 年から 2018 年に修正する
"""


def main():
    s = input().strip()
    modified = s.replace('2017', '2018')

    print(modified)


if __name__ == '__main__':
    main()
