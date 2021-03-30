# -*- coding: utf-8 -*-

# A - Airport Bus

"""
メモ
"""


def main():
    n: int  # 人数
    c: int  # バスの定員
    k: int  # 待てる時間
    n, c, k = map(int, input().strip().split())

    t = sorted(int(input().strip()) for _ in range(n))
    gone_bus_count = 0
    bus_passengers = 1
    first_passenger = t[0]
    for i in range(1, n):
        # バスが行ってしまった場合
        if bus_passengers >= c or t[i] > first_passenger + k:
            gone_bus_count += 1
            bus_passengers = 0

        # バスに人を乗せる
        if bus_passengers == 0:
            first_passenger = t[i]
            bus_passengers += 1
        elif bus_passengers < c and t[i] <= first_passenger + k:
            bus_passengers += 1

    if bus_passengers > 0:
        gone_bus_count += 1

    print(gone_bus_count)


if __name__ == '__main__':
    main()
