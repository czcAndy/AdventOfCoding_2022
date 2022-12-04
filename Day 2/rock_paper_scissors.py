import os

import requests
from itertools import product

with requests.Session() as s:
    s.cookies.set('session', os.environ['AOC_2022_COOKIE'])
    resp = s.get('https://adventofcode.com/2022/day/2/input')

matches = [item.decode('ascii').split() for item in resp.iter_lines()]

choices = ['ABC', 'XYZ']
possible_outcomes = list(map(list, (product(*choices))))

#1
possible_points = [4, 8, 3, 1, 5, 9, 7, 2, 6]
variants = list(zip(possible_points, possible_outcomes))
sum([variant[0] for variant in variants for match in matches if(match in variant)])


#2
possible_points = [3, 4, 8, 1, 5, 9, 2, 6, 7]
variants = list(zip(possible_points, possible_outcomes))
sum([variant[0] for variant in variants for match in matches if(match in variant)])
