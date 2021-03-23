# -*- coding: utf-8 -*-

# B - Billiards

"""
ビリヤード、x 軸を壁とする。
(S_x, S_y) にある球を撞いて 1 回反射させたのち、(G_x, G_y) を通過させるために x 軸のどこにぶつけるか。
"""


def main():
    s_x, s_y, g_x, g_y = map(int, input().strip().split())

    # tan_inc = (x - s_x) / s_y
    # tan_ref = (x - g_x) / g_y
    # tan_inc == tan_ref
    x = (s_x * g_y + g_x * s_y) / (s_y + g_y)

    print(x)


if __name__ == '__main__':
    main()
