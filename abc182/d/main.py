# -*- coding: utf-8 -*-

"""
なんとかしてループを 1 回にしたい
"""


def main():
    _ = int(input().strip())
    a = map(int, input().strip().split())

    robot_pos = 0
    max_robot_pos = 0
    accumulated_move_distances = [0]
    max_accumulated_move_distance = 0
    for x in a:
        accumulated_move_distances.append(accumulated_move_distances[-1] + x)
        max_accumulated_move_distance = max(max_accumulated_move_distance, accumulated_move_distances[-1])
        max_robot_pos = max(max_robot_pos, robot_pos + max_accumulated_move_distance)
        robot_pos += accumulated_move_distances[-1]
        max_robot_pos = max(max_robot_pos, robot_pos)

    print(max_robot_pos)


if __name__ == '__main__':
    main()
