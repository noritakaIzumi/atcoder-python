# -*- coding: utf-8 -*-

# A - Vanishing Pitch

"""
野球をしている。高橋君はピッチャー、青木君はバッター。
高橋君が投げる消える魔球は、速さ V m/s で等速直線運動をし、投げた瞬間から T 秒後から S 秒後まで消えている。
両端を含む。ボールは消えている間も移動を続ける。
ボールが高橋君のもとからちょうど D m 離れたときにボールが消えていなければ、青木君はボールを打つことができる。消えていれば打てない。
青木君は高橋君のボールを打つことができるか？
"""


def main():
    line = list(map(int, input().strip().split()))
    velocity = line[0]
    t = line[1]
    s = line[2]
    distance = line[3]
    if distance < velocity * t or velocity * s < distance:
        result = 'Yes'
    else:
        result = 'No'

    print(result)


if __name__ == '__main__':
    main()
