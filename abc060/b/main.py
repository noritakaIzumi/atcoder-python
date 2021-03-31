# -*- coding: utf-8 -*-

# B - Choose Integers

"""
総和は A * (自然数) にできる。
"""


class Result:
    yes = 'YES'
    no = 'NO'


def main():
    a, b, c = map(int, input().strip().split())

    x = 1
    ans = Result.no
    while x <= b:
        q, mod = divmod(a * x, b)
        if mod == c:
            ans = Result.yes
            break
        if mod == 0:
            break
        x += 1

    print(ans)


if __name__ == '__main__':
    main()
