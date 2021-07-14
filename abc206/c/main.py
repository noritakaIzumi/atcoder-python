# -*- coding: utf-8 -*-

"""
"""
from collections import Counter


def main():
    _ = int(input().strip())
    a = map(int, input().strip().split())

    counter = Counter(a)
    counter_values = counter.values()

    ans = (sum(counter_values) ** 2 - sum(map(lambda x: x ** 2, counter_values))) // 2
    print(ans)


if __name__ == '__main__':
    main()
