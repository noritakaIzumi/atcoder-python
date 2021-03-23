# -*- coding: utf-8 -*-

# A - Two Choices

"""
0 か 1 で答える M 問の問題がある。これに N 人の生徒が取り組んだ。
N 個の長さ M の文字列 S_1, S_2, ..., S_N が与えられる。
S_i の k 文字目は 0 か 1 のいずれかであり、i 番目の生徒の k 問目に対する回答を表す。
各生徒の各問題に対する回答は判明しているが、各問題の正解が 0 と 1 のどちらかは判明していない。

1 <= i < j <= N を満たす組で、生徒 i と生徒 j の正解した問題の数が等しい可能性がないようなものはいくつあるか。
"""


def main():
    n, m = map(int, input().strip().split())

    # 1 の数の偶奇が違う場合、正解数は一致し得ない
    students = [0, 0]
    for _ in range(n):
        students[input().strip().count('1') & 1] += 1
    print(students[0] * students[1])


if __name__ == '__main__':
    main()
