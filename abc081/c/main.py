# -*- coding: utf-8 -*-

# C - Not so Diverse

"""
メモ
"""
import collections


def main():
    k: int  # 目指すボールの種類数
    _, k = map(int, input().strip().split())
    a = map(int, input().strip().split())

    ball_counts = sorted(collections.Counter(a).values())
    ball_type_count = len(ball_counts)

    ans: int
    if ball_type_count <= k:
        ans = 0
    else:
        ans = sum(ball_counts[:ball_type_count - k])

    print(ans)


if __name__ == '__main__':
    main()
