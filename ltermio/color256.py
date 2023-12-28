#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright 2023 Brooks Su
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

r"""Sets 256-color display attributes of character terminal.

There are three pairs of functions to set or restore colors according
to their literal name:

    set_fcolor()
    reset_fcolor()

    set_bcolor()
    reset_bcolor()

    set_color()
    reset_color()

Enum class Color defined constants of some basic colors and grayscales,
and more colors can be generated by function make_color(r, g, b).

A simple sample as following:

    import ltermio
    from ltermio import Color

    ltermio.set_color(Color.GOLD, Color.BLUE)
    print('Hello, ltermio!')
    color = ltermio.make_color(4, 3, 1) # get a bronze color
    ltermio.set_fcolor(color)
    ...
    ltermio.reset_color()

Reference: https://en.wikipedia.org/wiki/ANSI_escape_code
"""

import enum

_CSI_LEAD = '\033['

def make_color(red: int, green: int, blue: int) -> int:
    r"""Returns a 256-color number according to the given RGB parameters.

    Args:
        All parameters' valid values must be in range of 0~5.

    Raises:
        ValueError: Argument value out of range.
    """
    if not (0 <= red <= 5 and 0 <= green <= 5 and 0 <= blue <= 5):
        raise ValueError('Argument value out of range.')
    return 16 + red * 36 + green * 6 + blue


class Color(enum.IntEnum):
    r"""Enumerates some common constants of colors.
    """
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    BRIGHT_BLACK = 8
    BRIGHT_RED = 9
    BRIGHT_GREEN = 10
    BRIGHT_YELLOW = 11
    BRIGHT_BLUE = 12
    BRIGHT_MAGENTA = 13
    BRIGHT_CYAN = 14
    BRIGHT_WHITE = 15

    GRAYSCALE_DARKEST = 232
    GRAYSCALE_DARK = 238
    GRAYSCALE_MIDDLE = 243
    GRAYSCALE_LIGHT = 249
    GRAYSCALE_LIGHTEST = 255
    GRAY = make_color(3, 3, 3)
    SILVER = make_color(4, 4, 4)

    TAN = make_color(5, 4, 3)
    BRONZE = make_color(4, 3, 1)
    COPPER = BRONZE
    COFFEE = make_color(2, 1, 0)
    CHOCOLATE = make_color(4, 2, 1)
    BROWN = make_color(3, 1, 1)

    PINK = make_color(5, 3, 3)
    HOT_PINK = make_color(5, 2, 4)
    DEEP_PINK = make_color(5, 0, 3)
    TOMATO = make_color(5, 2, 2)
    INDIAN_RED = TOMATO
    MAROON = RED
    CRIMSON = make_color(5, 0, 1)
    SCARLET = CRIMSON

    VIOLET = make_color(3, 0, 5)
    BRIGHT_VIOLET = make_color(5, 3, 5)
    ORCHID = make_color(3, 1, 5)
    BRIGHT_ORCHID = make_color(4, 2, 4)
    PLUM = make_color(5, 4, 5)
    LAVENDER = make_color(4, 4, 5)
    MEDIUM_PURPLE = make_color(3, 2, 5)
    PURPLE = make_color(3, 0, 3)

    INDIGO = make_color(1, 0, 4)
    NAVY = make_color(0, 0, 3)
    ROYAL_BLUE = make_color(2, 3, 5)
    SKY_BLUE = make_color(3, 5, 5)
    DEEP_SKY_BLUE = make_color(0, 4, 5)
    AZURE = make_color(4, 5, 5)

    TURQUOISE = make_color(2, 5, 4)
    SPRING_GREEN = make_color(2, 4, 3)
    SEA_GREEN = make_color(1, 4, 4)
    DEEP_SEA_GREEN = make_color(1, 3, 2)
    OLIVE = make_color(3, 3, 0)

    BEIGE = make_color(5, 5, 4)
    IVORY = BEIGE
    KHAKI = make_color(5, 5, 3)
    DEEP_KHAKI = make_color(4, 4, 2)
    GOLD = make_color(5, 4, 0)
    ORANGE = make_color(5, 3, 0)
    DEEP_ORANGE = make_color(5, 2, 0)


def set_fcolor(color: int):
    r"""Sets foreground color.
    """
    print(f'{_CSI_LEAD}38;5;{color}m', end='')


def reset_fcolor():
    r"""Restores the foreground color to the default value.
    """
    print(f'{_CSI_LEAD}39m', end='')


def set_bcolor(color: int):
    r"""Sets background color.
    """
    print(f'{_CSI_LEAD}48;5;{color}m', end='')


def reset_bcolor():
    r"""Restores the background color to the default value.
    """
    print(f'{_CSI_LEAD}49m', end='')


def set_color(fcolor: int, bcolor: int):
    r"""Sets foreground to 'fcolor' and background to 'bcolor'.
    """
    print(f'{_CSI_LEAD}38;5;{fcolor}m{_CSI_LEAD}48;5;{bcolor}m',
          end='')


def reset_color():
    r"""Restores foreground and background color to the default value.
    """
    print(f'{_CSI_LEAD}39;49m', end='')


def _test_color256():
    def color_block(color, width):
        set_bcolor(color)
        print(' ' * width, end='')
        reset_bcolor()

    def text_color():
        for i in range(6):
            for char in 'Hello, color256!':
                set_fcolor(ord(char) % 32 + 20 + i * 36)
                print(char, end='')
            print('')
        reset_fcolor()

    def grayscale():
        for color in range(Color.GRAYSCALE_DARKEST,
                           Color.GRAYSCALE_LIGHTEST + 1):
            color_block(color, 3)
        print('')

    def rgb():
        for red in range(6):
            for green in range(6):
                for blue in range(6):
                    color_block(make_color(red, green, blue), 2)
            print('')

    def constant_color():
        for color in sorted(Color):
            print(f'{color.name:18s}: {color.value:3d} ', end='')
            color_block(color, 12)
            print('')

    text_color()
    grayscale()
    rgb()
    constant_color()


if __name__ == '__main__':
    _test_color256()
