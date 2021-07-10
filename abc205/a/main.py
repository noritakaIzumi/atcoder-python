# -*- coding: utf-8 -*-

"""
100 mL あたり A kcal のドリンク B mL
"""


def main():
    a, b = map(int, input().strip().split())
    kcal = a * b / 100

    print(kcal)


if __name__ == '__main__':
    main()
