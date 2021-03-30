# -*- coding: utf-8 -*-

# C - Pyramid

"""
メモ
"""


class Pyramid:
    def __init__(self, cx: int, cy: int) -> None:
        self.cx = cx
        self.cy = cy

    def get_estimated_height(self, x: int, y: int, h: int) -> int:
        """得られた情報の h が 0 より大きいときに高さを求める。

        Args:
            x:
            y:
            h:

        Returns:
            int: height of the pyramid.

        """
        return h + abs(x - self.cx) + abs(y - self.cy)


def get_real_height(n: int, info: list) -> tuple:
    for x in range(101):
        for y in range(101):
            pyramid = Pyramid(x, y)
            estimated_height = pyramid.get_estimated_height(*info[0])
            is_correct = True
            for k in range(1, n):
                # 見当が違ったという判定
                if info[k][2] > 0 and pyramid.get_estimated_height(*info[k]) != estimated_height:
                    is_correct = False
                    break
                if info[k][2] <= 0 and estimated_height - abs(info[k][0] - x) - abs(info[k][1] - y) > 0:
                    is_correct = False
                    break
            if is_correct:
                return x, y, estimated_height


def main():
    n = int(input().strip())
    info = [list(map(int, input().strip().split())) for _ in range(n)]
    info.sort(key=lambda x: x[2], reverse=True)

    print('{} {} {}'.format(*get_real_height(n, info)))


if __name__ == '__main__':
    main()
