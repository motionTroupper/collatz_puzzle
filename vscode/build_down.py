#!/usr/bin/python3

import pieces.logic as logic
import pieces.colors as colors
import shutil
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number", type=str)
parser.add_argument("notation", choices=["d", "b"], nargs='?', default='d')
parser.add_argument("children", type=int,nargs='?', default=1)

args = parser.parse_args()

number = args.number
notation = args.notation
children = args.children

if notation == 'd':
    number = int(number)
elif notation == 'b':
    number = int(number, 2)
else:
    raise Exception('Invalid notation. Use d for decimal or b for binary.')


initial = logic.set_number(number)

rows = [initial]
initial = logic.bottom_numbers(initial, children)

for number in initial:
    rows.append(number)

for row in rows:
    print(colors.color_print(logic.spaced_pieces(row, spacer = '')).replace('E', '·'))
    print(colors.color_print(logic.spaced_binary(row, spacer = '')).replace('E', '·'))
    print (f"{int(logic.spaced_binary(row, spacer = '', separator=''),2):_}")
    print ()