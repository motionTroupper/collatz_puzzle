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
rows = [initial]

while not initial['is_power_of_two']:
    initial = logic.upper_number(initial)
    rows.insert(0, initial)

for row in rows:
    print(colors.color_print(logic.spaced_pieces(row)).replace('E', '·'))
    print(colors.color_print(logic.spaced_binary(row)).replace('E', '·'))
