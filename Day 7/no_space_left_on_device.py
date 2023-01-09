import os

import requests
from file_tree import *


def get_input():
    with requests.Session() as req:
        req.cookies.set('session', os.environ["AOC_2022_COOKIE"])
        resp = req.get('https://adventofcode.com/2022/day/7/input')
        return resp


def handle_cd_input(console_line, current_node, file_tree):
    folder_name = console_line.split()[-1]
    print("CD ", console_line, current_node.name)
    if folder_name == '..':
        return file_tree.get_parent(current_node)
    else:
        return current_node.get_adjacent_edge(folder_name)


def handle_ls_output(console_line, current_node, file_tree):
    print("LS ", console_line, current_node.name)
    if console_line.startswith("dir"):
        name = console_line.split()[-1]
        size = 0
    else:
        size, name = console_line.split()

    node = Node(name, size)
    file_tree.add_node(node)
    file_tree.add_edge(current_node, node)


def create_tree_structure_from_input():
    console_lines = get_input().iter_lines(decode_unicode=True)
    # Skip the cd / command. The tree can be initialized as below
    next(console_lines)

    file_tree = FileTree()
    current_node = Node("/", 0)
    file_tree.add_node(current_node)

    try:
        for console_line in console_lines:
            if console_line.startswith("$ cd"):
                current_node = handle_cd_input(console_line, current_node, file_tree)
            elif console_line == "$ ls":
                pass
            else:
                handle_ls_output(console_line, current_node, file_tree)
    except StopIteration:
        pass

    return file_tree


tree = create_tree_structure_from_input()
print(tree)
