# -*- coding: utf-8 -*-

# B - Making Triangle

"""
メモ
"""


def main():
    n = int(input().strip())
    pole = list(map(int, input().strip().split()))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if pole[i] == pole[j]:
                continue

            def condition(length: int) -> bool:
                different_length = length != pole[i] and length != pole[j]
                triangle_available = max(pole[i] - pole[j], pole[j] - pole[i]) < length < pole[i] + pole[j]
                return different_length and triangle_available

            ans += len(list(filter(condition, pole[j + 1:])))

    print(ans)


if __name__ == '__main__':
    main()
