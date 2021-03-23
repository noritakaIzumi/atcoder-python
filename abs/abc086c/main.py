# -*- coding: utf-8 -*-

# ABC086C - Traveling

"""
時刻 0: (0, 0)
次の目的地までの最短時間と予定時間との差が偶数なら 1 マス行って戻るを繰り返して暇つぶしすればよい。
"""


class Result:
    yes = 'Yes'
    no = 'No'


def main():
    n = int(input().strip())

    result = Result.no

    pos = [0, 0]
    current_time = 0
    for _ in range(n):
        t, x, y = map(int, input().strip().split())
        shortest = abs(x - pos[0]) + abs(y - pos[1])
        if current_time + shortest > t or (shortest ^ (t - current_time)) & 1:
            break
        pos = [x, y]
        current_time = t
    else:
        result = Result.yes

    print(result)


if __name__ == '__main__':
    main()
