# -*- coding: utf-8 -*-

# B - Palace

"""
標高 x メートル: 平均気温 T - 0.006 * x
"""


def main():
    n = int(input().strip())
    t, a = map(int, input().strip().split())
    h = list(map(int, input().strip().split()))

    def get_temp_diff(height: int) -> int:
        return abs(a * 1000 - t * 1000 + height * 6)

    best_spot_index = 0
    best_temp_diff = get_temp_diff(h[0])
    for i in range(1, n):
        temp_diff = get_temp_diff(h[i])
        if temp_diff < best_temp_diff:
            best_spot_index = i
            best_temp_diff = temp_diff

    print(best_spot_index + 1)


if __name__ == '__main__':
    main()
