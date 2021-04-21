# -*- coding: utf-8 -*-

"""
末尾から 0 を除いていって、回文になれば OK
"""
import re


class Result:
    yes = 'Yes'
    no = 'No'


def main():
    n = input()

    # 末尾から 0 を取り除く
    n = n[::-1]
    n = re.sub('^0*', '', n)
    ans = Result.yes if n == n[::-1] else Result.no

    print(ans)


if __name__ == '__main__':
    main()
