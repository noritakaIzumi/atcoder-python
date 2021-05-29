# -*- coding: utf-8 -*-

"""
"""


class Result:
    YES = 'Yes'
    NO = 'No'


def main():
    a = sorted(map(int, input().strip().split()))
    if a[0] + a[2] == a[1] * 2:
        result = Result.YES
    else:
        result = Result.NO

    print(result)


if __name__ == '__main__':
    main()
