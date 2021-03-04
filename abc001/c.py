# 入力を受け取る
array = [int(i) for i in input().rstrip().split()]

deg = array[0]  # 風光
dis = array[1]  # 風程


# 風程を求める
wind = None
if 0 <= dis < 15:
    wind = 0
elif dis < 93:
    wind = 1
elif dis < 201:
    wind = 2
elif dis < 327:
    wind = 3
elif dis < 477:
    wind = 4
elif dis < 645:
    wind = 5
elif dis < 831:
    wind = 6
elif dis < 1029:
    wind = 7
elif dis < 1245:
    wind = 8
elif dis < 1467:
    wind = 9
elif dis < 1707:
    wind = 10
elif dis < 1959:
    wind = 11
else:
    wind = 12

# 風向を求める
directions = [
    'N',
    'NNE',
    'NE',
    'ENE',
    'E',
    'ESE',
    'SE',
    'SSE',
    'S',
    'SSW',
    'SW',
    'WSW',
    'W',
    'WNW',
    'NW',
    'NNW'
]

direction = directions[(deg * 10 + 1125) % 36000 // 2250]
if wind == 0:
    direction = 'C'

# 結果出力
print(str(direction) + ' ' + str(wind))
