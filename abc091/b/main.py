# -*- coding: utf-8 -*-

# B - Two Colors Card Game

"""
メモ
"""
from typing import Dict


def main():
    word_balances: Dict[str, int]  # key=単語(str), value=収支(int)
    word_balances = {}

    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        if s not in word_balances.keys():
            word_balances[s] = 0
        word_balances[s] += 1

    m = int(input().strip())
    for _ in range(m):
        t = input().strip()
        if t not in word_balances.keys():
            word_balances[t] = 0
        word_balances[t] -= 1

    ans = max(max(word_balances.values()), 0)
    print(ans)


if __name__ == '__main__':
    main()
