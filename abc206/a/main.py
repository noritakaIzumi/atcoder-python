# -*- coding: utf-8 -*-

"""
消費税率 8 パーセント
税込み（切り捨て）が 206 円と比較してどうか
"""


class Result:
    cheap = 'Yay!'
    equal = 'so-so'
    expensive = ':('


def main():
    n = int(input().strip())

    tax_included = n * 1.08 // 1
    border = 206
    if tax_included < border:
        ans = Result.cheap
    elif tax_included == border:
        ans = Result.equal
    else:
        ans = Result.expensive

    print(ans)


if __name__ == '__main__':
    main()
