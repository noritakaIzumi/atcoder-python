# -*- coding: utf-8 -*-

# B - A to Z String

"""
メモ
"""


def main():
    s = input().strip()

    pos_a = s.find('A')
    pos_z = s.rfind('Z', pos_a)

    print(pos_z - pos_a + 1)


if __name__ == '__main__':
    main()
