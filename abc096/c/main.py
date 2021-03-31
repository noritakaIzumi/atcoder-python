# -*- coding: utf-8 -*-

# C - Grid Repainting 2

"""
1 マスだけぽつんと黒に塗らないといけない部分があったら No
上下左右 1 マスずつ白で余白を用意して if 文を減らす
"""


class Result:
    yes = 'Yes'
    no = 'No'


class Canvas:
    black = '#'
    white = '.'


def main():
    h, w = map(int, input().strip().split())
    s = [[Canvas.white for _ in range(w + 2)]]
    s += [[Canvas.white] + list(input().strip()) + [Canvas.white] for _ in range(h)]
    s += [[Canvas.white for _ in range(w + 2)]]

    result = Result.yes
    for i in range(1, h + 1):
        if result == Result.no:
            break
        for j in range(1, w + 1):
            if s[i][j] == Canvas.white:
                continue
            # 上下左右が全部白 -> アウト
            if s[i - 1][j] == s[i + 1][j] == s[i][j - 1] == s[i][j + 1] == Canvas.white:
                result = Result.no
                break

    print(result)


if __name__ == '__main__':
    main()
