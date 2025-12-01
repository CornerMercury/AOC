from os.path import dirname, join
import itertools


def decode_snafu(snafu):
    conv = {
        '2': 2,
        '1': 1,
        '0': 0,
        '-': -1,
        '=': -2
    }
    total = 0
    for i, count in enumerate([conv[char] for char in reversed(snafu)]):
        total += count * 5**i

    return total

def encode_snafu(num):
    conv = {
        2: '2',
        1: '1',
        0: '0',
        -1: '-',
        -2: '='
    }
    max_power = 0
    snafu = ''
    while num > sum([2 * 5**power for power in range(max_power+1)]):
        max_power += 1

    while max_power != -1:
        count = -2
        if max_power != 0:
            max_sum = sum([2 * 5**power for power in range(max_power)])
        else:
            return snafu + conv[num]
        while num - (count * 5**(max_power)) > max_sum:
            count += 1
        num -= (count * 5**max_power)
        snafu += conv[count]
        max_power -= 1
    
    return snafu
        



current_dir = dirname(__file__)
path = join(current_dir, "./25i.txt")

with open(path) as f:
  data = [line.strip('\n') for line in f.readlines()]

total = 0

for snafu in data:
    total += decode_snafu(snafu)

print(total)
print(encode_snafu(total))