# -*- coding: utf-8 -*-

# D - increment of coins

"""
袋の中に金貨 A 枚、銀貨 B 枚、銅貨 C 枚がある。
袋の中にあるいずれかの種類の硬貨が 100 枚になるまで以下の操作を繰り返す。

操作: 袋の中から硬貨を 1 枚ランダムに取り出す。取り出した硬貨と同じ種類の硬貨を 2 枚袋に戻す。

操作回数の期待値を求めよ。
"""
dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]


def get_expect(a: int, b: int, c: int) -> float:
    # if a == 0 and b == 0 and c == 0:
    #     return None
    if dp[a][b][c]:
        return dp[a][b][c]
    if a == 100 or b == 100 or c == 100:
        return 0
    ans = 0
    ans += get_expect(a + 1, b, c) * a
    ans += get_expect(a, b + 1, c) * b
    ans += get_expect(a, b, c + 1) * c
    ans /= a + b + c
    ans += 1
    dp[a][b][c] = ans
    return ans


def main():
    a, b, c = map(int, input().strip().split())
    result = '%.9f' % get_expect(a, b, c)
    print(result)


if __name__ == '__main__':
    main()
