# -*- coding: utf-8 -*-

# D - Div Game

"""
参考:
https://drken1215.hatenablog.com/entry/2020/06/01/010800
https://qiita.com/rute_not_route/items/0efb67d2706984c5fcf9

正の整数 N。N に対して、以下の操作を繰り返し行うことができる。
- はじめに、以下の条件をすべて満たす整数の整数 z を選ぶ。
    - ある素数 p と正の整数 e を用いて z = e^p と表せる。
    - N が z で割り切れる。
    - 以前の操作で選んだ度の整数とも異なる。
- N を N / z に置き換える。

最大で何回操作を行えるか求めよ。
"""
from typing import Dict


def get_factors(m: int) -> Dict[int, int]:
    sqrt = m ** 0.5

    index = 2
    fas = {}
    while index <= sqrt:
        while m % index == 0:
            if index not in fas.keys():
                fas[index] = 1
            else:
                fas[index] += 1
            m //= index
        index += 1

    if m != 1:
        fas[m] = 1

    return fas


def solve(n: int) -> int:
    if n == 1:
        return 0

    factors = get_factors(n)

    result = 0
    for count in factors.values():
        i = 1
        while count >= i:
            count -= i
            result += 1
            i += 1

    return result


def main():
    n = int(input().strip())
    print(solve(n))


if __name__ == '__main__':
    main()
