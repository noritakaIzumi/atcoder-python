# -*- coding: utf-8 -*-

# B - 文字列大好きいろはちゃんイージー

"""
メモ
"""


def main():
    n, _ = map(int, input().strip().split())

    print(''.join(sorted(input().strip() for _ in range(n))))


if __name__ == '__main__':
    main()
