# -*- coding: utf-8 -*-

"""
"""

import string

alphabet_by_id = list(string.ascii_lowercase)
id_by_alphabet = {v: k for k, v in enumerate(list(string.ascii_lowercase))}


class Result:
    Yes = 'Yes'
    No = 'No'


def main():
    s = list(input().strip())
    t = list(input().strip())

    shifts = {}
    for i, s_char in enumerate(s):
        shift = (id_by_alphabet[s_char] - id_by_alphabet[t[i]]) % 26
        shifts[shift] = True

    ans = Result.Yes if len(shifts) == 1 else Result.No
    print(ans)


if __name__ == '__main__':
    main()
