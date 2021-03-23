# -*- coding: utf-8 -*-

# ABC049C - 白昼夢

"""
eraser が唯一 er で始まり er で終わる。

・eraser は dream, dreamer, erase をどのような順番でつなげても登場させられない
・erase は dream, dreamer をどのような順番でつなげても登場させられない
・dreamer は dream をどのような順番でつなげても登場させられない
"""


class TargetWord:
    Dream = 'dream'
    Dreamer = 'dreamer'
    Erase = 'erase'
    Eraser = 'eraser'


class Result:
    YES = 'YES'
    NO = 'NO'


def main():
    s = input().strip()

    s = s.replace(TargetWord.Eraser, '')
    s = s.replace(TargetWord.Erase, '')
    s = s.replace(TargetWord.Dreamer, '')
    s = s.replace(TargetWord.Dream, '')

    if not s:
        result = Result.YES
    else:
        result = Result.NO

    print(result)


if __name__ == '__main__':
    main()
