from enum import Enum, auto

n = int(input().strip())


class RainEnum(Enum):
    start = auto()
    end = auto()


# 時刻を何分単位に丸めるか: 60 を割り切る数に設定
rain_time_unit = 5
units_per_hour = 60 // rain_time_unit


def rain_time_to_unit(time: str, rain: RainEnum) -> int:
    ret = int(time[:2]) * units_per_hour
    if rain == RainEnum.start:
        ret += int(time[2:]) // rain_time_unit
    elif rain == RainEnum.end:
        ret += (int(time[2:]) + (rain_time_unit - 1)) // rain_time_unit
    return ret


def unit_to_rain_time(unit: int) -> str:
    q, mod = divmod(unit, units_per_hour)
    return '%02d%02d' % (q, mod * rain_time_unit)


rains = {}
for _ in range(n):
    s = input().strip().split('-')
    start = rain_time_to_unit(s[0], RainEnum.start)
    end = rain_time_to_unit(s[1], RainEnum.end)
    if start not in rains.keys():
        rains[start] = 0
    if end not in rains.keys():
        rains[end] = 0
    rains[start] += 1
    rains[end] -= 1

rains = sorted(rains.items(), key=lambda x: x[0])

# Aggregate
current_rain = 0
rain_times = []
tmp_start = ''
for u, r in rains:
    if current_rain == 0 and r > 0:
        tmp_start = unit_to_rain_time(u)
    elif current_rain + r == 0:
        rain_times.append(f'{tmp_start}-{unit_to_rain_time(u)}')
    current_rain += r

print('\n'.join(rain_times))
