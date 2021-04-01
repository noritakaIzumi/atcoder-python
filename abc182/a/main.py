# -*- coding: utf-8 -*-

"""
"""


def main():
    a: int  # フォロワー数
    b: int  # フォロー数
    a, b = map(int, input().strip().split())

    follow_limit = 2 * a + 100
    ans = follow_limit - b
    print(ans)


if __name__ == '__main__':
    main()
