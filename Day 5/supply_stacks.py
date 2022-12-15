import os
import requests
from itertools import groupby

with requests.Session() as s:
    s.cookies.set("session", os.environ["AOC_2022_COOKIE"])
    resp = s.get("https://adventofcode.com/2022/day/5/input")


def get_input_and_instructions(resp):
    result = groupby(resp.iter_lines(), lambda ln: len(ln.strip()) == 0)
    result = [[g for g in group] for key, group in result]
    return result


def convert_input_matrix_to_string(matrix):
    result = [[item for item in input_line.decode("ascii")]
              for input_line in matrix]
    return result


def convert_instr_list_to_instr_matrix(instr_list):
    result = [[word for word in instr.decode("ascii").split(" ")
               if word != "move" and word != "to" and word != "from"]
              for instr in instr_list]

    result = [[int(no) for no in value] for value in result]

    return result


def is_blank(value):
    return value == ' '


def list_is_not_noise(column):
    return column[-1].isnumeric()


def remove_noise(matrix):
    clean_matrix = []
    for col_index in range(len(matrix[0])):
        if matrix[-1][col_index].isnumeric():
            clean_matrix.append(
                [matrix[item_index][col_index] for item_index in range(len(matrix))])
    return clean_matrix


def pretty_print(matrix):
    for row_index in matrix:
        print(row_index)


def perform_action(instruction, matrix):
    number_of_items_to_move, row_from, row_to = instruction
    row_from -= 1
    row_to -= 1

    items_to_be_moved = []
    number_of_items_to_be_moved = 0
    for row_item_index in range(len(matrix[row_from])):
        if not is_blank(matrix[row_from][row_item_index]) and number_of_items_to_be_moved < number_of_items_to_move:
            items_to_be_moved.append(matrix[row_from][row_item_index])
            matrix[row_from][row_item_index] = ' '
            number_of_items_to_be_moved += 1

    for row_item_index in range(len(matrix[row_to])):
        if not is_blank(matrix[row_to][row_item_index]):
            insert_index = row_item_index
            break

    spill_over = insert_index - len(items_to_be_moved)
    while spill_over < 0:
        matrix[row_to].insert(0, ' ')
        spill_over += 1

    for row_item_index in range(len(matrix[row_to])):
        if not is_blank(matrix[row_to][row_item_index]):
            for item_index in range(len(items_to_be_moved)):
                matrix[row_to][row_item_index - item_index - 1] = items_to_be_moved[-item_index - 1]
            break

    return matrix


input_matrix, _, instr_list = get_input_and_instructions(resp)
input_matrix = convert_input_matrix_to_string(input_matrix)
instr_list = convert_instr_list_to_instr_matrix(instr_list)

print(instr_list)

matrix = remove_noise(input_matrix)
for instr in instr_list:
    matrix = perform_action(instr, matrix)
    pretty_print(matrix)
    print("")
