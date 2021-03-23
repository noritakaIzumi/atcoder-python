# -*- coding: utf-8 -*-

# C - Travel

"""
メモ
"""
import itertools


def main():
    # n: 都市の数、k: 目指したい移動時間の合計
    n, k = map(int, input().strip().split())
    t = [list(map(int, input().strip().split())) for _ in range(n)]

    def get_path_count(time: int) -> int:
        result = 0
        for path in itertools.permutations(range(1, n), n - 1):
            current_city = 0
            current_time = 0
            for next_city in path:
                current_time += t[current_city][next_city]
                current_city = next_city
            current_time += t[current_city][0]
            if current_time == time:
                result += 1
        return result

    print(get_path_count(k))


if __name__ == '__main__':
    main()
