# -*- coding: utf-8 -*-

"""
"""
from typing import Callable


class Mountain:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height


def main():
    n = int(input().strip())
    mountains = []
    for _ in range(n):
        mountain = input().strip().split()
        mountains.append(Mountain(name=mountain[0], height=int(mountain[1])))

    func: Callable[[Mountain], int] = lambda m: m.height
    mountains.sort(key=func)

    result = mountains[-2].name
    print(result)


if __name__ == '__main__':
    main()
