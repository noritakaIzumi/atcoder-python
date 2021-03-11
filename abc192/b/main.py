# -*- coding: utf-8 -*-

# B - uNrEaDaBlE sTrInG

"""
先頭から奇数番目の文字が全て英小文字であり、かつ、先頭から偶数番目の文字が全て英大文字であるような文字列を「読みにくい文字列」とする。
文字列 S が「読みにくい文字列」なら Yes、そうでないなら No。
"""


def is_unreadable_string(s: str) -> bool:
    char: str
    for i, char in enumerate(s):
        index_is_odd = i & 1
        if not index_is_odd and char.islower():
            continue
        if index_is_odd and char.isupper():
            continue
        return False
    else:
        return True


def main():
    s = input().strip()
    result = 'Yes' if is_unreadable_string(s) else 'No'
    print(result)


if __name__ == '__main__':
    main()
