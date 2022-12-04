import os

import requests
from itertools import groupby

with requests.Session() as s:
    s.cookies.set('session', os.environ['AOC_2022_COOKIE'])
    resp = s.get('https://adventofcode.com/2022/day/1/input')

grouped_res = groupby(resp.iter_lines(), lambda x: x != b'')
grouped_res = [list(map(int, list(g))) for k, g in grouped_res if k]

# 1
print(max(map(sum, grouped_res)))

# 2
print(sorted(list(map(sum, grouped_res)))[-3:])
