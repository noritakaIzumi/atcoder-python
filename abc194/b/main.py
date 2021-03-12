# -*- coding: utf-8 -*-

# B - Job Assignment

"""
会社に従業員 1 から従業員 N までの N 人の従業員がいる。
仕事 A と仕事 B の 2 つの仕事を終えなければならない。
従業員 i は仕事 A を A_i 分、仕事 B を B_i 分で終わらせることができる。

仕事 A と仕事 B にそれぞれ従業員を 1 人割り当てる。
同じ従業員を両方の仕事に割り当てた場合、2 つの仕事が終わるのにかかる時間は、それぞれの仕事が終わるのにかかる時間の和。
2 つの仕事に異なる従業員を割り当てた場合、2 つの仕事が終わるのにかかる時間は、それぞれの仕事が終わるのにかかる時間の長い方。

2 つの仕事が終わるのにかかる時間として考えられる最小の値を求めよ。
"""


def main():
    n = int(input())
    employees = [list(map(int, input().strip().split())) for _ in range(n)]

    result = min(
        min(sum(employees[i]) if i == j else max(employees[i][0], employees[j][1]) for j in range(n)
            ) for i in range(n))
    print(result)


if __name__ == '__main__':
    main()
