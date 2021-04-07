# -*- coding: utf-8 -*-

"""
"""
from typing import Dict


def solve(n: int, r: Dict[int, set]) -> int:
    """

    Args:
        n (int): 議員数
        r (Relationship):

    Returns:
        int:

    """
    max_group = 0
    for i in range(1, 2 ** n):
        test_relation = set()
        for j in range(n):
            if i >> j & 1:
                test_relation.add(j + 1)
        for c in test_relation:
            if not test_relation.issubset(r[c]):
                break
        else:
            max_group = max(max_group, len(test_relation))

    return max_group


def main():
    n: int
    m: int
    relationships: Dict[int, set]
    n, m = map(int, input().strip().split())
    relationships = {i: {i} for i in range(1, n + 1)}

    if m == 0:
        ans = 1
    elif m == 1:
        ans = 2
    else:
        for _ in range(m):
            x, y = map(int, input().strip().split())
            relationships[x].add(y)
            relationships[y].add(x)
        ans = solve(n, relationships)

    print(ans)


if __name__ == '__main__':
    main()
