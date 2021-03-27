# -*- coding: utf-8 -*-

# B - Visibility

"""
メモ
"""


class Square:
    barrier = '#'
    nothing = '.'


def main():
    h, w, x, y = map(int, input().strip().split())
    s = [input().strip() for _ in range(h)]

    x -= 1
    y -= 1

    ans = 1  # count myself
    # to the left
    for j in range(y)[::-1]:
        if s[x][j] == Square.barrier:
            break
        else:
            ans += 1
    # to the right
    for j in range(y + 1, w):
        if s[x][j] == Square.barrier:
            break
        else:
            ans += 1
    # to the top
    for i in range(x)[::-1]:
        if s[i][y] == Square.barrier:
            break
        else:
            ans += 1
    # to the bottom
    for i in range(x + 1, h):
        if s[i][y] == Square.barrier:
            break
        else:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
