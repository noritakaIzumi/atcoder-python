# -*- coding: utf-8 -*-

# B - Two Anagrams

"""
メモ
"""


class Result:
    yes = 'Yes'
    no = 'No'


def dict_available(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t, reverse=True)

    while True:
        if not t:
            return False
        elif not s:
            return True

        if s[0] > t[0]:
            return False
        elif s[0] < t[0]:
            return True

        s = s[1:]
        t = t[1:]


def main():
    s = input().strip()
    t = input().strip()

    result = Result.yes if dict_available(s, t) else Result.no
    print(result)


if __name__ == '__main__':
    main()
