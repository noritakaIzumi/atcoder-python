# -*- coding: utf-8 -*-

# D - Snuke Prime

"""
すぬけプライムへの加入中は、1 日あたり C 円を支払うことで、提供される全てのサービスを追加料金の支払いなしに利用することができる。
すぬけプライムへの加入および脱退は、それぞれ 1 日の始めおよび終わりに自由に行うことができる。
"""
from typing import List, Tuple


class Service:
    def __init__(self, start: int, end: int, fee: int) -> None:
        """Constructor.

        Args:
            start (int): サービス利用開始日
            end (int): サービス利用終了日
            fee (int): すぬけプライムに加入していない場合にかかるサービスの値段（1 日あたり）
        """
        self.start = start
        self.end = end
        self.fee = fee


class Event:
    """値段の上下イベント。

    """

    def __init__(self, at: int, change: int) -> None:
        """Constructor.

        Args:
            at (int): 何日目に、
            change (int): 値段がどれくらい変動するか。
        """
        self.at = at
        self.change = change


# def get_sorted_events(services: List[Service]) -> List[Event]:
#     events = []
#     for service in services:
#         events.append(Event(service.start, service.fee))
#         events.append(Event(service.end + 1, - service.fee))
#     for i in range(1, len(events)):
#         for j in range(1, i + 1)[::-1]:
#             if events[j - 1].at > events[j].at:
#                 events[j - 1], events[j] = events[j], events[j - 1]
#     return events


class User:
    # def __init__(self, using_services: List[Service], prime_fee: int) -> None:
    # def __init__(self, events: List[Event], prime_fee: int) -> None:
    def __init__(self, events: List[Tuple[int, int]], prime_fee: int) -> None:
        """Constructor.

        Args:
            # using_services (:obj:`list` of Service): 利用するサービス。
            events (:obj:`list` of Event): 値段上下イベント。
            prime_fee (int): すぬけプライム 1 日当たりの料金。
        """
        # self.using_services = using_services
        self.prime_fee = prime_fee
        self.events = events

    def get_lowest_fee(self) -> int:
        total_fee = 0
        current_fee = 0
        events_count = len(self.events)
        for index in range(events_count - 1):
            # current_fee += self.events[index].change
            # total_fee += min(current_fee, self.prime_fee) * (self.events[index + 1].at - self.events[index].at)
            current_fee += self.events[index][1]
            total_fee += min(current_fee, self.prime_fee) * (self.events[index + 1][0] - self.events[index][0])
        return total_fee


def main():
    line = list(map(int, input().rstrip().split()))  # 利用するサービス数、すぬけプライム 1 日当たりの料金
    prime_fee = line[1]
    events = []
    for _ in range(line[0]):
        line = list(map(int, input().rstrip().split()))
        # events.append(Event(line[0], line[2]))
        # events.append(Event(line[1] + 1, - line[2]))
        events.append((line[0], line[2]))
        events.append((line[1] + 1, - line[2]))
    # for i in range(1, len(events)):
    #     for j in range(1, i + 1)[::-1]:
    #         if events[j - 1].at > events[j].at:
    #             events[j - 1], events[j] = events[j], events[j - 1]
    events.sort()
    # services = [Service(*map(int, input().rstrip().split())) for _ in range(line[0])]
    user = User(events, prime_fee)
    print(user.get_lowest_fee())


if __name__ == '__main__':
    main()
