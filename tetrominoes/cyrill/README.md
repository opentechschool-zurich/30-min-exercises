# Tetris

`tetris.c` is a Tetris implementation in C using `curses`, ANSI escape sequences
and UTF-8 box drawing and half block characters. It mostly follows the rules in
the Tetris Guidline.

## Controls

Use the home row (vi) or 'wasd' and the arrow keys.

| Keys             | Action        |
|------------------|---------------|
| (tab)            | swap hold     |
| (left), h        | shift left    |
| (right), l       | shift right   |
| (up), (space), k | hard drop     |
| (down), j        | soft drop     |
| a, s             | rotate left   |
| d, f             | rotate right  |
| q                | quit          |

## Build instructions

You can build `tetris.c` using the following command.

```bash
cc -Wall -lncurses -o tetris tetris.c
```

## System requirements

The game was tested using the Fira Code font in Kitty. Using a modern terminal
with UTF-8 support and a good terminal font is required for a decent experience.
