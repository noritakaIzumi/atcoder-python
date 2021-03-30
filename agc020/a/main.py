# -*- coding: utf-8 -*-

# A - Move and Win

"""
マス目は 1 * N。
奇数のマスから動かすと偶数のマス、偶数のマスから動かすと奇数のマスに行く。
1 マスごとに 2 色をローテーションで塗れば奇数のマスと偶数のマスで色がそれぞれ一致。

アリスとボリスがともに奇数またはともに偶数のマスなら、アリスが終わった時点でアリスとボリスの駒が隣り合うようにできる。
ボリスが端に行けばアリスが追い詰め、最終的にボリスが動けなくなり、アリスの勝利。

アリスとボリスの偶奇が異なる場合、先ほどの場合でボリスが先攻だと思えばボリスの勝利。
"""


class Result:
    alice = 'Alice'
    borys = 'Borys'
    draw = 'Draw'


def main():
    _, a, b = map(int, input().strip().split())

    ans = Result.borys if (a ^ b) & 1 else Result.alice
    print(ans)


if __name__ == '__main__':
    main()
