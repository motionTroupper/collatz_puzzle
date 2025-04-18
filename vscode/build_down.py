#!/usr/bin/python3

import pieces.logic as logic
import pieces.colors as colors
import shutil
import sys

if len(sys.argv) > 1:
    number = int(sys.argv[1], 2)
else:
    number = 0

initial = logic.set_number(number)
offset = initial['offset']

rows = [initial]
initial = logic.bottom_numbers(initial)
offset = max(offset, initial['offset'])
rows.append(initial)

for row in rows:
    print(colors.color_print(logic.spaced_pieces(row, spacer = '')).replace('E', '·'))
    print(colors.color_print(logic.spaced_binary(row, spacer = '')).replace('E', '·'))
