# -*- coding: utf-8 -*-

# B - Minesweeper

"""
メモ
"""


class Square:
    mine = '#'
    empty = '.'


class MineSweeper:
    def __init__(self, h: int, w: int, board: list) -> None:
        self.h = h
        self.w = w
        self.board = board

    def has_mine(self, i: int, j: int) -> bool:
        if 0 <= i <= self.h - 1 and 0 <= j <= self.w - 1 and self.board[i][j] == Square.mine:
            return True
        else:
            return False

    def get_mine_count(self, i: int, j: int) -> int:
        result = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if self.has_mine(i + x, j + y):
                    result += 1

        return result


def main():
    h, w = map(int, input().strip().split())
    mine_sweeper = MineSweeper(h, w, [list(input().strip()) for _ in range(h)])

    for i in range(h):
        for j in range(w):
            if mine_sweeper.board[i][j] == Square.mine:
                continue
            mine_sweeper.board[i][j] = str(mine_sweeper.get_mine_count(i, j))

    print('\n'.join(''.join(row) for row in mine_sweeper.board))


if __name__ == '__main__':
    main()
