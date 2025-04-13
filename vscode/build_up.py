#!/usr/bin/python3

import pieces.logic as logic
import pieces.colors as colors
import shutil
import sys

if len(sys.argv) > 1:
    number = int(sys.argv[1], 2)
else:
    number = 0

initial = logic.setNumber(number)
rows = [initial]
zeros = 0

while zeros != 1:
    initial, zeros = logic.upperNumber(initial)
    rows.insert(0, initial)
    if zeros == 1:
        break

for row in rows:
    print(colors.color_print(logic.spaced_pieces(row)).replace('E', '·'))
