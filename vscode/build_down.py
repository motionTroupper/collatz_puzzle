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
print (colors.color_print(logic.spaced_pieces(initial)).replace('E', '·'))
initial,zeros = logic.bottomNumbers(initial)
print (colors.color_print(logic.spaced_pieces(initial)).replace('E', '·'))

