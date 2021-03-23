# -*- coding: utf-8 -*-

# D - Water Heater

"""
お湯は溜めておけない
一度に使うお湯が毎分 W を超えなければ OK
"""


def main():
    # n: 人数, w: お湯のキャパシティ
    n, w = map(int, input().strip().split())

    # water_schedule: お湯使用予定
    # water_schedule[3]: 時刻 3 から 4 の間に使うお湯の量
    water_schedule = {}
    for _ in range(n):
        # s: お湯使用開始、t: お湯使用終了、p: 単位時間当たりお湯使用量
        s, t, p = map(int, input().strip().split())
        water_schedule_keys = water_schedule.keys()
        if s not in water_schedule_keys:
            water_schedule[s] = 0
        if t not in water_schedule_keys:
            water_schedule[t] = 0
        water_schedule[s] += p
        water_schedule[t] -= p

    water_schedule = sorted(water_schedule.items(), key=lambda x: x[0])

    result = 'No'
    current_capacity = w
    for _, usage_change in water_schedule:
        current_capacity -= usage_change
        if current_capacity < 0:
            break
    else:
        result = 'Yes'

    print(result)


if __name__ == '__main__':
    main()
