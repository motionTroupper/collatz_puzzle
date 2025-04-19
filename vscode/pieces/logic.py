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

def upper_number(source_row):
    bottom_row = source_row['pieces'][:]

    left_carry = None
    started = False
    row_pieces = []

    while bottom_row or left_carry:
        if bottom_row:
            bottom_piece = bottom_row.pop()
        else:
            bottom_piece = 'e'

        bottom_will_be = all_pieces[bottom_piece]['future']

        if bottom_will_be == 0 and not started:
            piece = "e"
        elif not started:
            piece = "s"
            started = True
        else:
            fitting_pieces = lookup_piece({
                "right": left_carry,
                "current": bottom_will_be
            })
            if 's' in fitting_pieces:
                fitting_pieces.remove('s')
            piece = fitting_pieces[0]

        if piece is None:
            raise ValueError("No piece found for the given criteria.")
            return None

        left_carry = all_pieces[piece]['left']
        row_pieces.insert(0, piece)

    return {
        'pieces':row_pieces,
        'is_power_of_two': is_power_of_two(row_pieces)
    }

def bottom_numbers(source_row, extended_positions):
    upper_row = source_row['pieces'][:]
    upper_size = len(upper_row)

    in_progress_rows = [ [] ]
    completed_rows = []

    while in_progress_rows:

        if upper_row:
            upper_piece = upper_row.pop(0)
        else:
            upper_piece = 'e'

        upper_is = all_pieces[upper_piece]['current']

        new_rows = []
        for row in in_progress_rows:

            if len(row) == 0:
                right_carry = 0
            else:
                right_carry = all_pieces[row[-1]]['right']

            fitting_pieces = lookup_piece(
                {
                    "left": right_carry,
                    "future": upper_is
                }
            )

            new_combo = False
            for piece in fitting_pieces:
                if new_combo:
                    current_row = row[:-1]
                    new_rows.append(current_row)
                else:
                    new_combo = True
                    current_row = row

                if piece=='s':
                    if upper_row:
                        current_row.append('x')
                    else:
                        current_row.append('s')
                elif piece == 'e':
                    if upper_row:
                        current_row.append('e')
                    else:
                        current_row.append('x')
                else:
                    current_row.append(piece)

        if new_rows: 
            in_progress_rows += new_rows

        next_rows=[]
        for row in in_progress_rows:
            if len(row)- upper_size > extended_positions:
                continue
            elif row[-1] == 'x':
                continue
            elif row[-1] == 's':
                completed_rows.append(row)
            else:
                next_rows.append(row)

        in_progress_rows = next_rows

    return [
        {
            'pieces': row,
            'is_power_of_two': is_power_of_two(row)
        } for row in completed_rows
    ]

def set_number(number):
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
            fitting_pieces = lookup_piece({
                "right": left_carry,
                "current": bit
            })
            if 's' in fitting_pieces:
                fitting_pieces.remove('s')
            piece = fitting_pieces[0]

        left_carry = all_pieces[piece]['left']
        row_pieces.insert(0, piece)

    return {
        'pieces':row_pieces,
        'is_power_of_two': is_power_of_two(row_pieces)
    }

def is_power_of_two(pieces):
    return binary_number(pieces).count('1') == 1

def binary_number(row):
    return ''.join(str(all_pieces[key]['current']) for key in row)

def decimal_number(row):
    return int(binary_number(row['pieces']), 2)

def spaced_binary(row, spacer = ' ', spaces=screen_width, separator= ' '):
    return (spacer * (spaces - 2 * len(row['pieces']) )) + separator.join(binary_number(row['pieces']))

def spaced_pieces(row, spacer = ' ', spaces=screen_width, separator=' '):
    return (spacer * (spaces - 2 * len(row['pieces']) )) + separator.join(row['pieces']).upper()
