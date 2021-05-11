# -*- coding: utf-8 -*-

"""
"""
import collections


def main():
    n = int(input().strip())

    def get_mod_by200(num: str) -> int:
        return int(num) % 200

    a = map(get_mod_by200, input().strip().split())

    counter = collections.Counter(a)

    ans = 0
    for v in counter.values():
        if v >= 2:
            ans += v * (v - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
