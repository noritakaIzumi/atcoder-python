# -*- coding: utf-8 -*-

# A - Addition

"""
偶数が 2 つあるいは奇数が 2 つ減って、偶数が 1 つ増える。

最初から奇数が 1 つの場合、
これを無くすことはできないので、偶数を 0 個にする必要がある。
偶数がある場合、1 個ずつ減らせるが 0 個にはできないので、初めから 0 個の場合に限る。
他、奇数が奇数個の場合、奇数が 1 個になったとき偶数が 0 個にはなり得ないので条件は達成できない。

最初から奇数が 0 個の場合、条件を達成できる。
他、奇数が偶数個の場合、奇数を 0 個にできて、条件を達成できる。
"""
import collections


class Answer:
    yes = 'YES'
    no = 'NO'


def main():
    n = int(input().strip())
    a = collections.Counter(map(lambda x: int(x) % 2, input().strip().split()))

    if a[1] % 2 == 0:
        ans = Answer.yes
    elif a[1] == 1 and a[0] == 0:
        ans = Answer.yes
    else:
        ans = Answer.no

    print(ans)


if __name__ == '__main__':
    main()
