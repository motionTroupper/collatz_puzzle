import random
import shutil

screen_width = shutil.get_terminal_size().columns

all_pieces = {
    "s": {"current": 1, "future": 0, "up": 0, "down": 1, "left": 2, "right": 0},
    "a": {"current": 1, "future": 1, "up": 1, "down": 1, "left": 2, "right": 2},
    "b": {"current": 0, "future": 0, "up": 0, "down": 0, "left": 1, "right": 2},
    "c": {"current": 1, "future": 0, "up": 0, "down": 1, "left": 2, "right": 1},
    "d": {"current": 0, "future": 1, "up": 1, "down": 0, "left": 0, "right": 1},
    "e": {"current": 0, "future": 0, "up": 0, "down": 0, "left": 0, "right": 0},
    "f": {"current": 1, "future": 1, "up": 1, "down": 1, "left": 1, "right": 0},
}

def lookup_piece(filter):
    return [
        key for key, values in all_pieces.items()
        if all(values.get(k) == v for k, v in filter.items())
    ]

def upperNumber(source_row):
    bottom_row = source_row[:]
    left_carry = None
    started = False
    upper_row = []
    ones = 0

    while bottom_row or left_carry:
        bottom_piece = bottom_row.pop() if bottom_row else 'e'
        bottom_will_be = all_pieces[bottom_piece]['future']

        if bottom_will_be == 0 and not started:
            piece = "e"
        elif not started:
            piece = "s"
            started = True
            ones += 1
        else:
            cell_pieces = lookup_piece({
                "right": left_carry,
                "current": bottom_will_be
            })
            if 's' in cell_pieces:
                cell_pieces.remove('s')
            piece = cell_pieces[0]
            ones += all_pieces[piece]['current']

        left_carry = all_pieces[piece]['left']
        upper_row.insert(0, piece)
    return upper_row, ones

def bottomNumbers(source_row):
    upper_row = source_row[:]
    right_carry = 0
    finished = False
    lower_row= []
    ones = 0

    while upper_row or right_carry or not finished:
        upper_piece = upper_row.pop() if upper_row else 'e'
        upper_is = all_pieces[upper_piece]['current']
        piece = None

        cell_pieces = lookup_piece({
            "left": right_carry,
            "future": upper_is
        })

        if 's' in cell_pieces and not upper_row:
            piece = 's'
            finished = True
        else:
            cell_pieces.remove('s') if 's' in cell_pieces else None
            piece = cell_pieces[random.randint(0, len(cell_pieces) - 1)]

        right_carry = all_pieces[piece]['right']
        ones += all_pieces[piece]['current']
        lower_row.insert(0, piece)

    return lower_row, ones

def setNumber(number):
    bits = list(str(bin(number))[2:])
    started = False
    left_carry = None
    row_pieces = []

    while left_carry or bits:
        bit = int(bits.pop()) if bits else 0
        if bit == 0 and not started:
            piece = "e"
        elif not started:
            piece = "s"
            started = True
        else:
            cell_pieces = lookup_piece({
                "right": left_carry,
                "current": bit
            })
            if 's' in cell_pieces:
                cell_pieces.remove('s')
            piece = cell_pieces[0]

        left_carry = all_pieces[piece]['left']
        row_pieces.insert(0, piece)
    return row_pieces

def binary_number(row):
    return ''.join(str(all_pieces[key]['current']) for key in row)

def decimal_number(row):
    return int(binary_number(row), 2)

def spaced_binary(row, spaces=screen_width):
    return (" " * (spaces - 2 * len(row))) + ' '.join(binary_number(row))

def spaced_pieces(row, spaces=screen_width):
    return (" " * (spaces - 2 * len(row))) + ' '.join(row).upper()
