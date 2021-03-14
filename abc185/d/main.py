# -*- coding: utf-8 -*-

# D - Stamp

"""
左右方向に N 個のマスが並んでいる。左から i 番目のマスをマス i と呼ぶことにする。
この N 個のマスのうち、マス A_1, A_2, A_3, ..., A_M の M 個のマスは青色で、それ以外のマスは白色。

一回だけ、正整数 k を選んで幅 k のハンコを作る。このハンコを 1 回使用すると、 N 個のマスのうち連続する k マスを選び、
それらを赤色に変えることができる。ただしその際、その k 個のマスの中に青色のマスが入っていてはならない。
k とハンコの使用方法をうまく決めたとき、最小で何回ハンコを使用すれば白色のマスが存在しない状態にできるか？
"""
import math


def main():
    line = list(map(int, input().strip().split()))
    n = line[0]
    m = line[1]

    if n == m:
        result = 0
    elif m == 0:
        result = 1
    else:
        pixels = sorted(map(int, input().strip().split()))
        intervals = [pixels[0] - 1] + [pixels[i + 1] - pixels[i] - 1 for i in range(m - 1)] + [n - pixels[m - 1]]
        intervals = list(filter(lambda i: i > 0, intervals))

        k = min(intervals)

        result = sum(math.ceil(interval / k) for interval in intervals)

    print(result)


if __name__ == '__main__':
    main()
