import os

import requests
from file_tree import *


def get_input():
    with requests.Session() as req:
        req.cookies.set('session', os.environ["AOC_2022_COOKIE"])
        resp = req.get('https://adventofcode.com/2022/day/7/input')
        return resp


def handle_cd_command(console_line, current_node, file_tree):
    folder_name = console_line.split()[-1]
    if folder_name == '..':
        parent_node = file_tree.get_parent(current_node)
        parent_node.add_size(current_node.get_size())
        return parent_node
    else:
        return current_node.get_adjacent_node(folder_name)


def handle_ls_output(console_line, current_node, file_tree):
    if console_line.startswith("dir"):
        name = console_line.split()[-1]
        size = 0
        is_directory = True
    else:
        size, name = console_line.split()
        is_directory = False

    node = Node(name, int(size), is_directory)
    file_tree.add_node(node)
    file_tree.add_edge(current_node, node)


def create_tree_structure_from_input():
    console_lines = get_input().iter_lines(decode_unicode=True)
    # Skip the cd / command. The tree can be initialized as below
    next(console_lines)

    file_tree = FileTree()
    current_node = Node("/", 0, True)
    file_tree.add_node(current_node)

    for console_line in console_lines:
        if console_line.startswith("$ cd"):
            current_node = handle_cd_command(console_line, current_node, file_tree)
        elif console_line == "$ ls":
            pass
        else:
            handle_ls_output(console_line, current_node, file_tree)

    return file_tree


tree = create_tree_structure_from_input()
print(tree.find_nodes_fulfill_point_a())
