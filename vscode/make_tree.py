#!/usr/bin/python3

import pieces.logic as logic
import pieces.colors as colors
import shutil
import sys
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("number", type=str)
parser.add_argument("notation", choices=["d", "b"], nargs='?', default='d')
parser.add_argument("children", type=int,nargs='?', default=5)
parser.add_argument("depth", type=int,nargs='?', default=4)

args = parser.parse_args()

number = args.number
notation = args.notation
children = args.children
depth = args.depth

if notation == 'd':
    number = int(number)
elif notation == 'b':
    number = int(number, 2)
else:
    raise Exception('Invalid notation. Use d for decimal or b for binary.')


def add_child_by_name(tree, target_name, new_child):
    if tree["number"] == target_name:
        tree.setdefault("children", []).append(new_child)
        return True  # found and added

    for child in tree.get("children", []):
        if add_child_by_name(child, target_name, new_child):
            return True

    return False  # not found

next_batch=[]
initial = logic.set_number(number)
next_batch.append(initial)

level = 0
while level < depth:
    level += 1
    pending = next_batch
    next_batch = []
    while pending:
        current = pending.pop(0)
        for number in logic.bottom_numbers(current, children):
            add_child_by_name(initial,current['number'],{'number':number['number']})
            next_batch.append(number)


print(json.dumps(initial, indent=2))