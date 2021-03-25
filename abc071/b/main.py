# -*- coding: utf-8 -*-

# B - Not Found

"""
メモ
"""
import string

alphabet = {char: False for char in string.ascii_lowercase}


def main():
    s = input().strip()
    for c in s:
        alphabet[c] = True

    ans = 'None'
    for char in alphabet:
        if not alphabet[char]:
            ans = char
            break

    print(ans)


if __name__ == '__main__':
    main()
