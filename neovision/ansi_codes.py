# global definitions for ansi escape codes

reset = '\u001b[0m'

# colors
black = '\u001b[0;30m'
red = '\u001b[0;31m'
green = '\u001b[0;32m'
brown = '\u001b[0;33m'
blue = '\u001b[0;34m'
purple = '\u001b[0;35m'
cyan = '\u001b[0;36m'
light_gray = '\u001b[0;37m'
dar_gray = '\u001b[0;30m'
l_red = '\u001b[0;31m'
l_green = '\u001b[0;32m'
yellow = '\u001b[0;33m'
l_blue = '\u001b[0;34m'
l_purple = '\u001b[0;35m'
l_cyan = '\u001b[0;36m'
white = '\u001b[0;37m'

# background colors
bg_black = '\u001b[0;40m'
bg_red = '\u001b[0;41m'
bg_green = '\u001b[0;42m'
bg_yellow = '\u001b[0;43m'
bg_blue = '\u001b[0;44m'
bg_magenta = '\u001b[0;45m'
bg_cyan = '\u001b[0;46m'
bg_white = '\u001b[0;47m'
bg_br_black = '\u001b[40;1m'
bg_br_red = '\u001b[41;1m'
bg_br_green = '\u001b[42;1m'
bg_br_yellow = '\u001b[43;1m'
bg_br_blue = '\u001b[44;1m'
bg_br_magenta = '\u001b[45;1m'
bg_br_cyan = '\u001b[46;1m'
bg_br_white = '\u001b[47;1m'

bold = '\u001b[1m'


# cursor moves
def cursor_up(n):
    return u'\u001b[' + str(n) + 'A'


def cursor_down(n):
    return u'\u001b[' + str(n) + 'B'


def cursor_right(n):
    return u'\u001b[' + str(n) + 'C'


def cursor_left(n):
    return u'\u001b[' + str(n) + 'D'
