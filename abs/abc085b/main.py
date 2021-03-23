# -*- coding: utf-8 -*-

# ABC085B - Kagami Mochi

"""
同じ直径の餅は 1 回しか使えない。
"""


def main():
    n = int(input().strip())

    uniq_mochi = {}
    for _ in range(n):
        uniq_mochi[input().strip()] = True

    print(len(uniq_mochi.keys()))


if __name__ == '__main__':
    main()
