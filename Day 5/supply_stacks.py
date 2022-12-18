import os
import requests
from itertools import groupby

with requests.Session() as s:
    s.cookies.set("session", os.environ["AOC_2022_COOKIE"])
    resp = s.get("https://adventofcode.com/2022/day/5/input")


def get_input_and_instructions(resp):
    result = groupby(resp.iter_lines(), lambda ln: len(ln.strip()) == 0)
    result = [[g.decode("ascii") for g in group] for key, group in result]
    return result


def is_noise(value):
    return value in [" ", "]", "[", "move", "to", "from"]


def transpose(matrix):
    return list(zip(*matrix))


def duplicate_matrix(matrix):
    return [row[:] for row in matrix]


def clean_input(matrix):
    clean_matrix = []
    for row in matrix:
        if not all(is_noise(item) for item in row):
            clean_matrix.append([item for item in row if not is_noise(item) and not item.isnumeric()])
    return clean_matrix


def clean_instructions(instr_list):
    return [[int(word) for word in instr.split(" ")
             if not is_noise(word)]
            for instr in instr_list]


def perform_action_part_1(instruction, matrix):
    start_index, row_from_index, row_to_index = [i - 1 for i in instruction]

    matrix[row_to_index] = matrix[row_from_index][start_index::-1] + matrix[row_to_index]
    del matrix[row_from_index][start_index::-1]

    return matrix


def perform_action_part_2(instruction, matrix):
    stop_index, row_from_index, row_to_index = [i - 1 for i in instruction]

    matrix[row_to_index] = matrix[row_from_index][0:stop_index + 1] + matrix[row_to_index]
    del matrix[row_from_index][0:stop_index + 1]

    return matrix


def calculate_answer(matrix, instr_list, action_function):
    matrix_cp = duplicate_matrix(matrix)
    for instr in instr_list:
        matrix_cp = action_function(instr, matrix_cp)

    for rows in matrix_cp:
        print(rows[0])


input_matrix, _, instr_list = get_input_and_instructions(resp)
input_matrix = transpose(input_matrix)
input_matrix = clean_input(input_matrix)
instr_list = clean_instructions(instr_list)

# Part 1
calculate_answer(input_matrix, instr_list, perform_action_part_1)
# Part 2
calculate_answer(input_matrix, instr_list, perform_action_part_2)
