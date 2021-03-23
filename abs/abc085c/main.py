# -*- coding: utf-8 -*-

# ABC085C - Otoshidama

"""
1000 円札を 5000 円札に変えると、枚数の合計は 4 枚減る。
1000 円札を 10000 円札に変えると、枚数の合計は 9 枚減る。
"""


def otoshidama(n: int, y: int) -> list:
    only1000_count = y // 1000
    target_diff = only1000_count - n

    if target_diff == 0:
        return [0, 0, only1000_count]

    if 10000 * n < y:
        return [-1, -1, -1]

    possible_diffs = {}
    for i in range(target_diff % 4, min(target_diff // 9 + 1, n + 1), 4):
        for j in range(min((target_diff - 9 * i) // 4 + 1, n - i + 1)):
            if 9 * i + 4 * j not in possible_diffs.keys():
                possible_diffs[9 * i + 4 * j] = [[i, j]]
            else:
                possible_diffs[9 * i + 4 * j].append([i, j])

    if target_diff not in possible_diffs.keys():
        return [-1, -1, -1]

    for diff in possible_diffs[target_diff]:
        if 10000 * diff[0] + 5000 * diff[1] + 1000 * (n - sum(diff)) == y:
            return [diff[0], diff[1], n - sum(diff)]

    return [-1, -1, -1]


def main():
    n, y = map(int, input().strip().split())
    print(' '.join(map(str, otoshidama(n, y))))


if __name__ == '__main__':
    main()
