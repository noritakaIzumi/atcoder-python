# -*- coding: utf-8 -*-

"""
"""


def main():
    n = int(input().strip())
    a = map(int, input().strip().split())

    counter = [0 for _ in range(n + 1)]
    for m in a:
        counter[m] = 1

    result = 'No'
    if min(counter[1:]) == 1:
        result = 'Yes'

    print(result)


if __name__ == '__main__':
    main()
