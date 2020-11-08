import sys
import time
from ansi_codes import *

counter = 0
clock = time.CLOCK_MONOTONIC
prev = time.clock_gettime_ns(clock)
n_lines = 30
fps_counter = 0
while True:
    color_list = [red, blue, green]
    line = u'' + color_list[counter % 3] + '000000000000000000000000000000000000000000000000000000000000000000000' \
                                           '000000000000000000000000000000000000000000000000000\n'
    for i in range(n_lines):
        sys.stdout.write(line)
    #sys.stdout.write(cursor_left(120))
    sys.stdout.write(cursor_up(n_lines))
    cur = time.clock_gettime_ns(clock)

    if time.clock_gettime_ns(clock) - prev >= 1000000000:
        prev = time.clock_gettime_ns(clock)
        sys.stdout.write(cursor_down(n_lines))
        sys.stdout.write(u'' + white + bg_br_red + 'FPS: ' + '{:5.0f}'.format(fps_counter))
        sys.stdout.write(cursor_left(10))
        sys.stdout.write(cursor_up(n_lines))
        fps_counter = 0
        counter += 1
    sys.stdout.flush()
    fps_counter += 1


