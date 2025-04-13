import re

colors = {
    "RED": "\033[31m",
    "RESET": "\033[0m",
    "DARK": "\033[2m",
    "BLUE": "\033[34m",
}

color_maps = [
    ['(  D.B.)', 'RED', '\\1', 0],
]

def color_print(text):
    for pattern, color_name, repl, count in color_maps:
        color = colors.get(color_name, '')
        text = re.sub(pattern, f"{color}{repl}{colors['RESET']}", text, count=count)
    return text
