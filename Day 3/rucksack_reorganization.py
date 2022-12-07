import os

import requests
from itertools import chain


def get_input():
    with requests.Session() as s:
        s.cookies.set('session', os.environ['AOC_2022_COOKIE'])
        resp = s.get("https://adventofcode.com/2022/day/3/input")
    return resp


small_letters = list(range(ord('a'), ord('z') + 1))
capital_letters = list(range(ord('A'), ord('Z') + 1))
all_letters = small_letters + capital_letters


def sliced_line(line):
    first_half = set(line[slice(len(line) // 2)])
    second_half = set(line[slice(len(line) // 2, len(line))])

    return first_half & second_half


def sum_letter_values(letter_list):
    return sum([all_letters.index(item) + 1 for item in letter_list])


def chunk_input(values, s):
    return zip(*[iter(values)] * s)


# 1
total_sum = sum([sum_letter_values(sliced_line(line)) for line in get_input().iter_lines()])
print(total_sum)

# 2
intersecting_values = chain(*[set.intersection(*map(set, line)) for line in chunk_input(get_input().iter_lines(), 3)])
print(sum_letter_values(intersecting_values))