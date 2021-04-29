# -*- coding: utf-8 -*-

"""
"""


class Result:
    yes = 'Yes'
    no = 'No'


def main():
    a, b, c = map(int, input().strip().split())
    condition = a ** 2 + b ** 2 < c ** 2

    if condition:
        ans = Result.yes
    else:
        ans = Result.no

    print(ans)


if __name__ == '__main__':
    main()
