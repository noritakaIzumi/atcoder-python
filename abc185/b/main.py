# -*- coding: utf-8 -*-

# B - Smartphone Addiction

"""
スマートフォンがあり、バッテリーは N [mAh]。
時刻 n + 0.5 (n は整数) を迎えるたびにバッテリー残量が 1 [mAh] ずつ減少する。

高橋君はスマートフォンを満充電した状態で時刻 0 に外出し、途中で M 回カフェを訪れ、時刻 T に帰宅する。
i 回目に訪れるカフェには時刻 A_i から 時刻 B_i まで滞在する。
カフェにいる間はスマートフォンを充電するため、バッテリー残量は減少せず、
代わりに時刻 n + 0.5 (n は整数) を迎えるたびにバッテリー残量が 1 [mAh] ずつ増加する。
ただし、既にバッテリー残量がバッテリー容量と等しい場合、バッテリー残量は増えも減りもしない。

高橋君が途中でスマートフォンのバッテリー残量が 0 になることなく帰宅することができるかを判定せよ。
帰宅できる: Yes、帰宅できない: No。
"""


class SmartphoneAddiction:
    """高橋君はスマートフォン依存症。

    Attributes:
        smartphone_capacity (int): バッテリー容量
        current_battery (int): 現在のバッテリー残量
        go_home_time (int): 帰宅時刻
        current_time (int): 現在時刻
    """

    def __init__(self, smartphone_capacity: int, go_home_time: int) -> None:
        """Constructor.

        Args:
            smartphone_capacity (int): バッテリー容量
            go_home_time (int): 帰宅時刻

        """
        self.smartphone_capacity = smartphone_capacity
        self.current_battery = self.smartphone_capacity
        self.go_home_time = go_home_time
        self.current_time = 0

    def cafe(self, arrive: int, leave: int) -> None:
        self.decrease_battery(arrive - self.current_time)
        self.increase_battery(leave - arrive)
        self.current_time = leave

    def go_home(self) -> None:
        self.decrease_battery(self.go_home_time - self.current_time)
        self.current_time = self.go_home_time

    def decrease_battery(self, amount: int) -> None:
        self.current_battery = max(self.current_battery - amount, 0)
        if self.current_battery == 0:
            raise SmartphoneAddiction.BatteryDeadError

    def increase_battery(self, amount: int) -> None:
        self.current_battery = min(self.current_battery + amount, self.smartphone_capacity)

    class BatteryDeadError(ValueError):
        pass


class Result:
    YES = 'Yes'
    NO = 'No'


def main():
    line = list(map(int, input().strip().split()))
    takahashi = SmartphoneAddiction(line[0], line[2])

    try:
        for _ in range(line[1]):
            line = map(int, input().strip().split())
            takahashi.cafe(*line)
        takahashi.go_home()
    except SmartphoneAddiction.BatteryDeadError:
        print(Result.NO)
        return

    print(Result.YES)


if __name__ == '__main__':
    main()
