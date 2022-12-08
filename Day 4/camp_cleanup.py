import os

import requests


def get_input():
    with requests.Session() as s:
        s.cookies.set('session', os.environ["AOC_2022_COOKIE"])
        resp = s.get("https://adventofcode.com/2022/day/4/input")
        return resp


def split_pairs(ln):
    pairs = [convert_string_to_int(v) for v in (p.split('-') for p in ln.split(','))]
    return pairs


def convert_string_to_int(value):
    return [int(v) for v in value]


def ranges_are_subsets(l1, l2):
    return (l1[0] >= l2[0] and l1[1] <= l2[1]) or (l2[0] >= l1[0] and l2[1] <= l1[1])


def ranges_overlap(l1, l2):
    return not(l1[1] < l2[0] or l1[0] > l2[1])


# 1
input_values = [ranges_are_subsets(*split_pairs(line.decode("ascii"))) for line in get_input().iter_lines()]
print(input_values.count(True))

# 2
input_values = [ranges_overlap(*split_pairs(line.decode("ascii"))) for line in get_input().iter_lines()]
print(input_values.count(True))
