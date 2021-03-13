# -*- coding: utf-8 -*-

# B - Many Oranges

"""
みかんがいっぱいあって、すべて重さが A グラム以上 B グラム以下であることがわかっている。
この中からいくつかのみかんを選んだところ、選んだみかんの重さがちょうど W キログラムになった。
選んだみかんの個数として考えられる最小値と最大値を求める。このようなことが起こりえない場合、UNSATISFIABLE を出力する。

Notes:
    みかんの個数で考えられる合計の重さの範囲の中に W キログラムが含まれていればよい。
    (みかんを x 個選んだ時の) 最小の重さ <= W <= 最大の重さ、みたいな感じ。
"""
import math


class Result:
    UNSATISFIABLE = 'UNSATISFIABLE'


class OrangeCountRange:
    def __init__(self, minimum: int, maximum: int) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def to_display(self) -> str:
        return f'{self.minimum} {self.maximum}'


class UnsatisfiableError(ValueError):
    pass


def get_orange_count_range(min_weight: int, max_weight: int, weight_sum: int) -> OrangeCountRange:
    # 最小値・最大値の候補
    minimum = math.ceil(weight_sum * 1000 / max_weight)
    maximum = weight_sum * 1000 // min_weight
    if minimum <= maximum:
        return OrangeCountRange(minimum, maximum)
    raise UnsatisfiableError


def main():
    line = map(int, input().strip().split())

    result: str
    try:
        result = get_orange_count_range(*line).to_display()
    except UnsatisfiableError:
        result = Result.UNSATISFIABLE
    print(result)


if __name__ == '__main__':
    main()
