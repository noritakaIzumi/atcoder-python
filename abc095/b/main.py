# -*- coding: utf-8 -*-

# B - Bitter Alchemy

"""
ドーナツ i を作るとお菓子の素 m_i グラムを消費
全種類のドーナツを最低 1 個作るという条件下で、最大何個ドーナツ作れるか？

1 個ずつ作ったらあとはお菓子の素一番消費しないやつを永遠に作る
"""


def main():
    n, x = map(int, input().strip().split())

    material_min = 1000
    material_sum = 0
    for _ in range(n):
        m = int(input().strip())
        material_min = min(material_min, m)
        material_sum += m

    ans = n + (x - material_sum) // material_min
    print(ans)


if __name__ == '__main__':
    main()
