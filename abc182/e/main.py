# -*- coding: utf-8 -*-

"""
"""


class Cell:
    dark = '.'
    light = '+'
    lighted = '*'
    block = '#'


def main():
    h, w, n, m = map(int, input().strip().split())

    board = [list(Cell.block * (w + 2))]
    for _ in range(h):
        board.append(list(Cell.block + Cell.dark * w + Cell.block))
    board.append(list(Cell.block * (w + 2)))

    for _ in range(n):
        x, y = map(int, input().strip().split())
        board[x][y] = Cell.light

    for _ in range(m):
        x, y = map(int, input().strip().split())
        board[x][y] = Cell.block

    # 縦方向の精査
    for i_1 in range(1, h + 1):
        block_pos = [j_1 for j_1, x in enumerate(board[i_1]) if x == Cell.block]
        for b_1 in range(len(block_pos) - 1):
            if Cell.light in board[i_1][block_pos[b_1] + 1:block_pos[b_1 + 1]]:
                for k_1 in range(block_pos[b_1] + 1, block_pos[b_1 + 1]):
                    if board[i_1][k_1] == Cell.dark:
                        board[i_1][k_1] = Cell.lighted

    # 横方向の精査
    for j_2 in range(1, w + 1):
        block_pos = [i_2 for i_2 in range(h + 2) if board[i_2][j_2] == Cell.block]
        for b_2 in range(len(block_pos) - 1):
            if Cell.light in [board[i_2][j_2] for i_2 in range(block_pos[b_2] + 1, block_pos[b_2 + 1])]:
                for k_2 in range(block_pos[b_2] + 1, block_pos[b_2 + 1]):
                    if board[k_2][j_2] == Cell.dark:
                        board[k_2][j_2] = Cell.lighted

    # 光が届いていないマスを数える -> 全マス数から引く
    lighted_cell_count = 0
    for i in range(1, h + 1):
        lighted_cell_count += board[i].count(Cell.lighted) + board[i].count(Cell.light)

    print(lighted_cell_count)


if __name__ == '__main__':
    main()
