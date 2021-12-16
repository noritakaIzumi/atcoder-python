# -*- coding: utf-8 -*-

"""
"""


def main():
    candidates = {}

    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        if s not in candidates:
            candidates[s] = 0
        candidates[s] += 1

    ans = max(candidates, key=candidates.get)
    print(ans)


if __name__ == '__main__':
    main()
