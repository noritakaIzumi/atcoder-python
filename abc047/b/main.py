# -*- coding: utf-8 -*-

# B - すぬけ君の塗り絵 2 イージー

"""
a_i = 1, 2, 3, 4 のそれぞれについて、塗られる部分の最大を考える
"""


def main():
    w, h, n = map(int, input().strip().split())

    painted = {'x': {'left': 0, 'right': w}, 'y': {'bottom': 0, 'top': h}}
    for _ in range(n):
        x, y, a = map(int, input().strip().split())
        if a == 1:
            painted['x']['left'] = max(x, painted['x']['left'])
        elif a == 2:
            painted['x']['right'] = min(x, painted['x']['right'])
        elif a == 3:
            painted['y']['bottom'] = max(y, painted['y']['bottom'])
        elif a == 4:
            painted['y']['top'] = min(y, painted['y']['top'])

    white_area = 1
    white_area *= max(painted['x']['right'] - painted['x']['left'], 0)
    white_area *= max(painted['y']['top'] - painted['y']['bottom'], 0)

    print(white_area)


if __name__ == '__main__':
    main()
