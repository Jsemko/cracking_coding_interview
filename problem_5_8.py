"""
inputs are an array of bytes, (8 bit ints), each bit representing a pixel
width which is divisible by 8
x1 and x2 which as positions in the x direction
y height
goal: draw horizontal line on screen from x1 to x2
"""

import numpy as np

def check_screen(screen, w):

    assert screen.dtype ==  np.uint8, 'screen needs to hold 8 bit ints'
    assert screen.ndim == 1
    assert w % 8 == 0, 'width is not multiple of 8'
    array_w = w // 8
    assert screen.size % array_w == 0
    pass

def to_str(n):
    return format(n, '8b').replace('0', ' ').replace('1', '-')

def print_screen(screen, w):

    check_screen(screen, w)
    array_w = w // 8
    array_h = screen.size // array_w

    for i in range(array_h):
        curr_row = screen[i * array_w: (i + 1) * array_w ]
        print(''.join([to_str(n) for n in curr_row]))

def draw_horizontal_line(screen, w, x1, x2, y):


    check_screen(screen, w)
    array_w = w // 8
    array_h = screen.size // array_w

    screen[:] = 0 # want a blank screen to start

    insert_row = np.zeros(array_w, dtype=np.uint8)

    x1_int = x1 // 8
    x1_idx = x1 % 8
    x2_int = x2 // 8
    x2_idx = x2 % 8

    insert_row[x1_int:x2_int+1] = 255
    insert_row[x1_int] &= ((1 << (8 - x1_idx)) - 1)
    insert_row[x2_int] &= ~((1 << (8 - x2_idx - 1)) - 1)

    screen[y * array_w: (y + 1) * array_w ] = insert_row

    print_screen(screen, w)

screen = np.zeros(12, dtype=np.uint8)
w = 24

draw_horizontal_line(screen, w, 4, 10, 0)
print('*'*80)
draw_horizontal_line(screen, w, 3, 6, 1)

