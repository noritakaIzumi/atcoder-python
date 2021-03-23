# -*- coding: utf-8 -*-

# ABC081B - Shift only

"""
メモ
"""


def main():
    n = int(input().strip())
    a = map(int, input().strip().split())

    result = 0
    while True:
        divided = list(map(lambda x: divmod(x, 2), a))
        if max(list(map(lambda x: x[1], divided))) == 0:
            result += 1
            a = map(lambda x: x[0], divided)
        else:
            break

    print(result)


if __name__ == '__main__':
    main()
