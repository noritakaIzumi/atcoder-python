# -*- coding: utf-8 -*-

# B - Counting Roads

"""
メモ
"""


def main():
    n, m = map(int, input().strip().split())

    road_counts = [0 for _ in range(n + 1)]
    for _ in range(m):
        road = map(int, input().strip().split())
        for p in road:
            road_counts[p] += 1

    print('\n'.join(map(str, road_counts[1:])))


if __name__ == '__main__':
    main()
