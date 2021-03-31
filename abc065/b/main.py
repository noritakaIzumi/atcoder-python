# -*- coding: utf-8 -*-

# B - Trained?

"""
一度光ったことのあるボタンがまた光るような状況になると、無限ループしてボタン 2 にたどりつけないので NG。
光ったことあるボタンリストを作る。
"""


def main():
    n = int(input().strip())
    buttons = {i: int(input().strip()) for i in range(1, n + 1)}

    lighted = 1
    lighted_history = {1}
    ans = 0
    while lighted != 2:
        if buttons[lighted] in lighted_history:
            ans = -1
            break
        lighted_history.add(buttons[lighted])
        lighted = buttons[lighted]
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
