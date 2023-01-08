import os
import requests


def get_input():
    with requests.Session() as req:
        req.cookies.set('session', os.environ['AOC_2022_COOKIE'])
        resp = req.get('https://adventofcode.com/2022/day/6/input')
        return resp


def is_start_sequence(seq):
    return all([seq.count(sample) == 1 for sample in seq])


def find_distinct_signal(signal, sample_size):
    seq = [next(signal) for _ in range(sample_size + 1)]
    index = sample_size

    if is_start_sequence(seq):
        return index

    while not is_start_sequence(seq):
        seq.pop(0)
        seq.append(next(signal))
        index += 1

    return index


# part 1
signal_1 = get_input().iter_content(decode_unicode=True)
print(find_distinct_signal(signal_1, 4))

# part 2
signal_2 = get_input().iter_content(decode_unicode=True)
print(find_distinct_signal(signal_2, 14))
