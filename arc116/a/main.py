# -*- coding: utf-8 -*-

# A - Odd vs Even

"""
メモ
"""


class Answer:
    same = 'Same'
    odd = 'Odd'
    even = 'Even'


def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        q, mod = divmod(n, 2)
        if mod == 1:
            ans = Answer.odd
        elif q % 2 == 1:
            ans = Answer.same
        else:
            ans = Answer.even

        print(ans)


if __name__ == '__main__':
    main()
