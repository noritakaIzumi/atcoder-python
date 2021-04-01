# -*- coding: utf-8 -*-

"""
"""


def main():
    n = int(input().strip())

    points = [list(map(int, input().strip().split()))]
    max_square_length = 0
    for _ in range(n - 1):
        p = list(map(int, input().strip().split()))
        for point in points:
            square_length = ((point[0] - p[0]) ** 2 + (point[1] - p[1]) ** 2)
            max_square_length = max(max_square_length, square_length)
        points.append(p)

    print(max_square_length ** 0.5)


if __name__ == '__main__':
    main()
