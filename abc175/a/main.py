# -*- coding: utf-8 -*-

"""
"""
from typing import NewType, List

weather = NewType('weather', str)

sunny: weather = weather('S')
rainy: weather = weather('R')


def continuous_rainy_days(weathers: List[weather]) -> int:
    max_rainy_days = 0
    current_rainy_days = 0
    for w in weathers:
        if w == sunny:
            current_rainy_days = 0
        elif w == rainy:
            current_rainy_days += 1
            if current_rainy_days > max_rainy_days:
                max_rainy_days = current_rainy_days

    return max_rainy_days


def main():
    s: List[weather] = list(input().strip())
    print(continuous_rainy_days(s))


if __name__ == '__main__':
    main()
