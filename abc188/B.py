# -*- coding: utf-8 -*-

# B - Orthogonality

"""
ベクトルが 2 つ与えられて、その内積が 0 かどうか判断する。
"""
from enum import Enum
from typing import List


class Vector:
    def __init__(self, degree: int, component: List[int]):
        if degree != len(component):
            raise ValueError('次元と成分数が違います')
        self._degree = degree
        self._component = component

    @classmethod
    def get_inner_product(cls, v1: __init__, v2: __init__) -> int:
        if v1._degree != v2._degree:
            raise ValueError('次元が違います')
        return sum(v1._component[i] * v2._component[i] for i in range(v1._degree))


def is_orthogonal(vector1: Vector, vector2: Vector) -> bool:
    return Vector.get_inner_product(vector1, vector2) == 0


class YesOrNoEnum(Enum):
    YES = 'Yes'
    NO = 'No'


def main():
    degree = int(input())
    c1, c2 = [list(map(int, input().rstrip().split())) for _ in range(2)]
    vector1 = Vector(degree, c1)
    vector2 = Vector(degree, c2)
    print(YesOrNoEnum.YES.value if is_orthogonal(vector1, vector2) else YesOrNoEnum.NO.value)


if __name__ == '__main__':
    main()
