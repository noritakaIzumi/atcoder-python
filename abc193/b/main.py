# -*- coding: utf-8 -*-

# B - Play Snuke

"""
人気ゲーム機「スヌケマシン」がある。
スヌケマシンを販売している店は店 1, 2, ..., N の N 軒あり、
店 i は高橋君の現在地から徒歩 A_i 分、スヌケマシンの販売価格は P_i 円、現在のスヌケマシンの在庫は X_i 台。

高橋君は今から徒歩でスヌケマシンを販売してる店に向かい、店についたときにスヌケマシンの在庫があればスヌケマシンを飼う。
今から 0.5, 1.5, 2.5, ... 分後にすべての店でスヌケマシンの在庫が（存在するなら）1 台減る。
高橋君がスヌケマシンを買うことができるかどうか判定し、できる場合は買うのに必要な最小の金額を出力する。できない場合は -1 を出力する。

Notes:
    買えるお店の条件は A_i < X_i となる。
    この条件を満たす店のうち、販売価格が最も安いものがあればそれを出力すればよい。
"""


def main():
    n = int(input())
    min_price = 10 ** 9 + 1
    for _ in range(n):
        shop = list(map(int, input().strip().split()))
        a = shop[0]
        p = shop[1]
        x = shop[2]
        if a < x:
            min_price = min(min_price, p)
    result = min_price if min_price < 10 ** 9 + 1 else -1
    print(result)


if __name__ == '__main__':
    main()
