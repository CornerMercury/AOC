from aocd import get_data, submit
from functools import cmp_to_key

YEAR = 2023


def get_type(hand):
    max_label = max(hand.count(c) for c in hand)
    num_different_cards = len({*hand})
    if max_label == 5:
        return 6
    if max_label == 4:
        return 5
    if num_different_cards == 2:
        return 4
    if max_label == 3:
        return 3
    if num_different_cards == 3:
        return 2
    if num_different_cards == 4:
        return 1
    return 0


def compare_hands(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    type1 = get_type(hand1)
    type2 = get_type(hand2)
    if type1 - type2 != 0:
        return type1 - type2
    else:
        for c, d in zip(hand1, hand2):
            ic = "23456789TJQKA".index(c)
            id = "23456789TJQKA".index(d)
            if ic - id != 0:
                return ic - id
        return 0


def compare_hands_joker(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]

    if hand1 != "JJJJJ":
        most_common_hand1 = sorted(
            hand1, key=lambda x: hand1.replace("J", "").count(x)
        )[-1]
    else:
        most_common_hand1 = "J"
    if hand2 != "JJJJJ":
        most_common_hand2 = sorted(
            hand2, key=lambda x: hand2.replace("J", "").count(x)
        )[-1]
    else:
        most_common_hand2 = "J"
    type1 = get_type(hand1.replace("J", most_common_hand1))
    type2 = get_type(hand2.replace("J", most_common_hand2))
    if type1 - type2 != 0:
        return type1 - type2
    else:
        for c, d in zip(hand1, hand2):
            ic = "J23456789TQKA".index(c)
            id = "J23456789TQKA".index(d)
            if ic - id != 0:
                return ic - id
        return 0


def part1(data):
    l = map(str.split, data.split("\n"))
    sort_l = sorted(l, key=cmp_to_key(compare_hands))
    res = 0
    for i in range(len(sort_l)):
        res += (i + 1) * int(sort_l[i][1])
    return res


def part2(data):
    l = map(str.split, data.split("\n"))
    sort_l = sorted(l, key=cmp_to_key(compare_hands_joker))
    res = 0
    for i in range(len(sort_l)):
        res += (i + 1) * int(sort_l[i][1])
    return res


data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def main():
    day = int(__file__.split("\\")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
