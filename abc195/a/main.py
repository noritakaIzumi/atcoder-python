# -*- coding: utf-8 -*-

# A - Health M Death

"""
高橋君がモンスターと戦っている。
高橋君が魔法を使うと、体力が M の倍数であるモンスターを倒すことができる。それ以外のモンスターには効果なし。
高橋君の魔法によって、体力が H のモンスターを倒すことができるか？
"""


class Result:
    YES = 'Yes'
    NO = 'No'


def monster_knocked_down(multiple: int, hp: int) -> bool:
    return hp % multiple == 0


def main():
    line = map(int, input().strip().split())
    knocked_down = monster_knocked_down(*line)
    print(Result.YES if knocked_down else Result.NO)


if __name__ == '__main__':
    main()
