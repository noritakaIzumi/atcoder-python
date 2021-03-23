# -*- coding: utf-8 -*-

# B - Maximum Difference

"""
メモ
"""


def main():
    _ = int(input().strip())
    a = sorted(map(int, input().strip().split()))

    print(a[-1] - a[0])


if __name__ == '__main__':
    main()
