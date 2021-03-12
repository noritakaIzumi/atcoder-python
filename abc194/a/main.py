# -*- coding: utf-8 -*-

# A - I Scream

"""
アイスクリーム
・乳固形分が 15 パーセント以上、乳脂肪分が 8 パーセント以上含まれるもの: アイスクリーム
・上に当てはまらず、乳固形分が 10 パーセント以上、乳脂肪分が 3 パーセント以上含まれるもの: アイスミルク
・上のいずれにも当てはまらず、乳固形分が 3 パーセント以上含まれるもの: ラクトアイス
・上のいずれにも当てはまらないもの: 氷菓

※乳固形分は無脂乳固形分と乳脂肪分からなる

「スヌケアイス」には無脂乳固形分は A パーセント、乳脂肪分は B パーセント含まれるとすると、上の分類のうちどれに当てはまるか？
・スヌケアイスがアイスクリームに当てはまる場合 : 1
・スヌケアイスがアイスミルクに当てはまる場合 : 2
・スヌケアイスがラクトアイスに当てはまる場合 : 3
・スヌケアイスが氷菓に当てはまる場合 : 4
"""
from enum import Enum


class IceCreamEnum(Enum):
    ICE_CREAM = 1
    ICE_MILK = 2
    LACTO_ICE = 3
    FROZEN_DESSERT = 4


def get_ice_cream_class(a: int, b: int) -> IceCreamEnum:
    solids: int = a + b  # Milk solids
    fat: int = b  # Milk fat
    if solids >= 15 and fat >= 8:
        return IceCreamEnum.ICE_CREAM
    elif solids >= 10 and fat >= 3:
        return IceCreamEnum.ICE_MILK
    elif solids >= 3:
        return IceCreamEnum.LACTO_ICE
    else:
        return IceCreamEnum.FROZEN_DESSERT


def main():
    line = list(map(int, input().strip().split()))
    print(get_ice_cream_class(*line).value)


if __name__ == '__main__':
    main()
