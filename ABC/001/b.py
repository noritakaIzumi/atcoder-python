# Standard Input
distance = int(input())

# 単位変換
distanceInMeter = distance / 1000.0

# VVに変換する
if distanceInMeter < 0.1:
    vv = 0
elif distanceInMeter <= 5:
    vv = distanceInMeter * 10
elif distanceInMeter <= 30:
    vv = distanceInMeter + 50
elif distanceInMeter <= 70:
    vv = (distanceInMeter - 30) / 5 + 80
else:
    vv = 89

# Print Result
print('%02d' % vv)
