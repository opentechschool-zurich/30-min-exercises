#include <curses.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// TODO point count
// TODO speed levels

#define FIELD_WIDTH 10
#define FIELD_HEIGHT 20

const uint8_t STDIN = 0;

const uint8_t LOCK_DELAY = 30; // frames

const uint8_t FPS = 60;

const char UTF8_LOWER_HALF_BLOCK[] = {0xe2, 0x96, 0x84, 0x00};

typedef uint8_t bool_t;

typedef enum color {
  COLOR_ANSI_BLACK,
  COLOR_ANSI_YELLOW,
  COLOR_ANSI_BRIGHT_RED,
  COLOR_ANSI_BRIGHT_GREEN,
  COLOR_ANSI_BRIGHT_YELLOW,
  COLOR_ANSI_BRIGHT_BLUE,
  COLOR_ANSI_BRIGHT_MAGENTA,
  COLOR_ANSI_BRIGHT_CYAN
} color_t;

uint8_t color_ansi_fg(color_t color);
uint8_t color_ansi_bg(color_t color);

typedef struct vec2 {
  uint8_t x, y;
} vec2_t;

void vec2_rotate_right(uint8_t count, vec2_t *vec2s);
void vec2_rotate_left(uint8_t count, vec2_t *vec2s);

typedef enum piece_orientation {
  PIECE_ORIENTATION_0,
  PIECE_ORIENTATION_R,
  PIECE_ORIENTATION_2,
  PIECE_ORIENTATION_L
} piece_orientation_t;

const vec2_t OFFSETS_JLSTZ[4][5] = {
    {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},
    {{0, 0}, {1, 0}, {1, -1}, {0, 2}, {1, 2}},
    {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},
    {{0, 0}, {-1, 0}, {-1, -1}, {0, 2}, {-1, 2}}};

const vec2_t OFFSETS_I[4][5] = {{{0, 0}, {-1, 0}, {2, 0}, {-1, 0}, {2, 0}},
                                {{-1, 0}, {0, 0}, {0, 0}, {0, 1}, {0, -2}},
                                {{-1, 1}, {1, 1}, {-2, 1}, {1, 0}, {-2, 0}},
                                {{0, 1}, {0, 1}, {0, 1}, {0, -1}, {0, 2}}};

const vec2_t OFFSETS_O[4][5] = {{{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},
                                {{0, -1}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},
                                {{-1, -1}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},
                                {{-1, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}}};

typedef struct piece {
  color_t color;
  vec2_t tiles[4];
  const vec2_t (*offsets)[4][5];
} piece_t;

const piece_t I = {.color = COLOR_ANSI_BRIGHT_CYAN,
                   .tiles = {{-1, 0}, {0, 0}, {1, 0}, {2, 0}},
                   .offsets = &OFFSETS_I};
const piece_t J = {.color = COLOR_ANSI_BRIGHT_BLUE,
                   .tiles = {{-1, 1}, {-1, 0}, {0, 0}, {1, 0}},
                   .offsets = &OFFSETS_JLSTZ};
const piece_t L = {.color = COLOR_ANSI_YELLOW,
                   .tiles = {{-1, 0}, {0, 0}, {1, 0}, {1, 1}},
                   .offsets = &OFFSETS_JLSTZ};
const piece_t O = {.color = COLOR_ANSI_BRIGHT_YELLOW,
                   .tiles = {{0, 1}, {1, 1}, {0, 0}, {1, 0}},
                   .offsets = &OFFSETS_O};
const piece_t S = {.color = COLOR_ANSI_BRIGHT_GREEN,
                   .tiles = {{0, 1}, {1, 1}, {-1, 0}, {0, 0}},
                   .offsets = &OFFSETS_JLSTZ};
const piece_t T = {.color = COLOR_ANSI_BRIGHT_MAGENTA,
                   .tiles = {{-1, 0}, {0, 0}, {1, 0}, {0, 1}},
                   .offsets = &OFFSETS_JLSTZ};
const piece_t Z = {.color = COLOR_ANSI_BRIGHT_RED,
                   .tiles = {{-1, 1}, {0, 1}, {0, 0}, {1, 0}},
                   .offsets = &OFFSETS_JLSTZ};

typedef struct dynamic_piece {
  piece_orientation_t orientation;
  vec2_t position;
  uint8_t lock_delay;
  piece_t piece;
} dynamic_piece_t;

void dynamic_piece_init(dynamic_piece_t *dynamic_piece, const piece_t *piece);

typedef struct frame_timer {
  struct timespec start;
  struct timespec interval;
} frame_timer_t;

void frame_timer_init(frame_timer_t *timer);

void frame_timer_reset(frame_timer_t *timer);

bool_t frame_timer_tick(frame_timer_t *timer);

typedef struct game {
  uint8_t fall_countdown;
  frame_timer_t frame_timer;
  dynamic_piece_t dynamic_piece;
  color_t field[FIELD_HEIGHT][FIELD_WIDTH];
} game_t;

void game_init(game_t *game);

void game_render(game_t *game);

void game_handle_input(game_t *game);

void game_rotate_right(game_t *game);

void game_rotate_left(game_t *game);

void game_shift_right(game_t *game);

void game_shift_left(game_t *game);

// return 1 if piece was placed
bool_t game_fall(game_t *game);

void game_remove_full_lines(game_t *game);

// return 0 when placement is not possible
bool_t game_adjust_placement(game_t *game, dynamic_piece_t *dynamic_piece);

// return 1 if piece collides with game
bool_t game_check_collision(game_t *game, dynamic_piece_t *dynamic_piece);

int main(int argc, char *argv[]) {
  initscr();
  raw();
  keypad(stdscr, TRUE);
  noecho();

  if (curs_set(0) == ERR) {
    fprintf(stderr, "error: cannot set cursor invisible\n");
    return 1;
  }

  {
    int flags = fcntl(STDIN, F_GETFL, 0);
    fcntl(STDIN, F_SETFL, flags | O_NONBLOCK);
  }

  game_t game;
  game_init(&game);
  frame_timer_reset(&game.frame_timer);
  game.fall_countdown = 30;

  while (true) { // game loop
    if (frame_timer_tick(&game.frame_timer)) {
      if (game.fall_countdown > 0) {
        game.fall_countdown--;
      } else {
        game.fall_countdown = 30;
        game_fall(&game);
      }
      game_handle_input(&game);
      game_render(&game);
    }
    napms(1);
  }

  curs_set(2);
  endwin();
  return 0;
}

void frame_timer_init(frame_timer_t *timer) {
  timer->interval.tv_sec = 0;
  timer->interval.tv_nsec = 1000000000L / FPS;
}

void frame_timer_reset(frame_timer_t *timer) {
  clock_gettime(CLOCK_MONOTONIC_RAW, &timer->start);
}

uint8_t frame_timer_tick(frame_timer_t *timer) {
  struct timespec now, diff;
  clock_gettime(CLOCK_MONOTONIC_RAW, &now);
  diff.tv_sec = now.tv_sec - timer->start.tv_sec;
  diff.tv_nsec = now.tv_nsec - timer->start.tv_nsec;
  if (diff.tv_sec > timer->interval.tv_sec ||
      (diff.tv_sec == timer->interval.tv_sec &&
       diff.tv_nsec >= timer->interval.tv_nsec)) {
    timer->start.tv_nsec += timer->interval.tv_nsec;
    timer->start.tv_sec +=
        timer->interval.tv_sec + timer->start.tv_nsec / 1000000000;
    timer->start.tv_nsec = timer->start.tv_nsec % 1000000000;
    return 1;
  }
  return 0;
}

void game_init(game_t *game) {
  memset(game, 0, sizeof(game_t));
  frame_timer_init(&game->frame_timer);
  dynamic_piece_init(&game->dynamic_piece, &L);
}

void game_render(game_t *game) {
  color_t field_buffer[FIELD_HEIGHT][FIELD_WIDTH];
  memcpy(field_buffer, game->field,
         FIELD_HEIGHT * FIELD_WIDTH * sizeof(color_t));
  const dynamic_piece_t *dynamic_piece = &game->dynamic_piece;
  const piece_t *piece = &dynamic_piece->piece;
  for (uint8_t i = 0; i < 4; i++) {
    const vec2_t screen_position = {
        .x = dynamic_piece->position.x + piece->tiles[i].x,
        .y = FIELD_HEIGHT - (dynamic_piece->position.y + piece->tiles[i].y)};
    field_buffer[screen_position.y][screen_position.x] = piece->color;
  }
  for (uint8_t y = 0; y < FIELD_HEIGHT; y += 2) {
    for (uint8_t x = 0; x < FIELD_WIDTH; x++) {
      printf("\033[%d;%df\033[%d;%dm%s", y / 2 + 1, x + 1,
             color_ansi_fg(field_buffer[y + 1][x]),
             color_ansi_bg(field_buffer[y][x]), UTF8_LOWER_HALF_BLOCK);
    }
  }
}

void game_handle_input(game_t *game) {
  switch(getch()) {
  case KEY_LEFT:
  case 'h':
    game_shift_left(game);
    break;
  case KEY_RIGHT:
  case 'l':
    game_shift_right(game);
    break;
  case 'a':
  case 's':
    game_rotate_left(game);
    break;
  case 'd':
  case 'f':
    game_rotate_right(game);
    break;
  case 'q':
    curs_set(2);
    endwin();
    exit(0);
    break;
  case KEY_UP:
  case ' ':
  case 'k':
    while (!game_fall(game));
    break;
  case KEY_DOWN:
  case 'j':
    game_fall(game);
    break;
  default:
    break;
  }
}

void game_rotate_right(game_t *game)
{
  dynamic_piece_t rotated = game->dynamic_piece;
  vec2_rotate_right(4, rotated.piece.tiles);
  rotated.orientation = (rotated.orientation + 1) % 4;
  if (game_adjust_placement(game, &rotated)) {
    game->dynamic_piece = rotated;
    game->fall_countdown = LOCK_DELAY;
  }
}

void game_rotate_left(game_t *game)
{
  dynamic_piece_t rotated = game->dynamic_piece;
  vec2_rotate_left(4, rotated.piece.tiles);
  rotated.orientation = (rotated.orientation + 3) % 4;
  if (game_adjust_placement(game, &rotated)) {
    game->dynamic_piece = rotated;
    game->fall_countdown = LOCK_DELAY;
  }
}

void game_shift_right(game_t *game) {
  dynamic_piece_t shifted = game->dynamic_piece;
  shifted.position.x++;
  if (!game_check_collision(game, &shifted)) {
    game->dynamic_piece = shifted;
    game->fall_countdown = LOCK_DELAY;
  }
}

void game_shift_left(game_t *game) {
  dynamic_piece_t shifted = game->dynamic_piece;
  shifted.position.x--;
  if (!game_check_collision(game, &shifted)) {
    game->dynamic_piece = shifted;
    game->fall_countdown = LOCK_DELAY;
  }
}

bool_t game_fall(game_t *game) {
  dynamic_piece_t shifted = game->dynamic_piece;
  shifted.position.y--;
  if (game_check_collision(game, &shifted)) {
    const vec2_t position = game->dynamic_piece.position;
    const piece_t *piece = &game->dynamic_piece.piece;
    for (uint8_t i = 0; i < 4; i++) {
      const vec2_t screen_position = {.x = position.x + piece->tiles[i].x,
                                      .y = FIELD_HEIGHT -
                                           (position.y + piece->tiles[i].y)};
      game->field[screen_position.y][screen_position.x] = piece->color;
    }
    game_remove_full_lines(game);
    // TODO reinit random piece
    dynamic_piece_init(&game->dynamic_piece, &T);
    if (game_check_collision(game, &game->dynamic_piece)) {
      // TODO handle end of game
      curs_set(2);
      endwin();
      printf("\033[2J\033[1;1f\033[31;40mYou lose!\n");
      exit(0);
    }
    game->fall_countdown = 30; // TODO use speed level
    return 1;
  } else {
    game->dynamic_piece.position.y--;
    return 0;
  }
}

void game_remove_full_lines(game_t *game) {
  for (uint8_t y = FIELD_HEIGHT - 1; y >> 0; y--) {
    bool_t line_full = 1;
    for (uint8_t x = 0; x < FIELD_WIDTH; x++) {
      if (game->field[y][x] == 0) {
        line_full = 0;
        break;
      }
    }
    if (line_full) {
      memmove(&game->field[1], game->field, y * FIELD_WIDTH * sizeof(color_t));
    }
  }
}

bool_t game_adjust_placement(game_t *game, dynamic_piece_t *dynamic_piece) {
  const vec2_t position = dynamic_piece->position;
  const vec2_t(*offsets)[4][5] = dynamic_piece->piece.offsets;
  const vec2_t(*from_offsets)[5] = &(*offsets)[game->dynamic_piece.orientation];
  const vec2_t(*to_offsets)[5] = &(*offsets)[dynamic_piece->orientation];
  for (uint8_t i = 0; i < 5; i++) {
    dynamic_piece->position.x = position.x + ((*from_offsets)[i].x - (*to_offsets)[i].x);
    dynamic_piece->position.y = position.y + ((*from_offsets)[i].y - (*to_offsets)[i].y);
    if (!(game_check_collision(game, dynamic_piece))) {
      return 1;
    }
  }
  return 0;
}

bool_t game_check_collision(game_t *game, dynamic_piece_t *dynamic_piece) {
  const vec2_t position = dynamic_piece->position;
  const piece_t *piece = &dynamic_piece->piece;
  for (uint8_t i = 0; i < 4; i++) {
    const vec2_t tile = {.x = position.x + piece->tiles[i].x,
                         .y = FIELD_HEIGHT - (position.y + piece->tiles[i].y)};
    if (tile.x < 0 || tile.x > FIELD_WIDTH - 1 || tile.y < 0 ||
        tile.y > FIELD_HEIGHT - 1 || game->field[tile.y][tile.x])
      return 1;
  }
  return 0;
}

void vec2_rotate_right(uint8_t count, vec2_t *vec2s) {
  for (uint8_t i = 0; i < count; i++) {
    const vec2_t src = vec2s[i];
    vec2s[i].x = src.y;
    vec2s[i].y = -src.x;
  }
}

void vec2_rotate_left(uint8_t count, vec2_t *vec2s) {
  for (uint8_t i = 0; i < count; i++) {
    const vec2_t src = vec2s[i];
    vec2s[i].x = -src.y;
    vec2s[i].y = src.x;
  }
}

void dynamic_piece_init(dynamic_piece_t *dynamic_piece, const piece_t *piece) {
  memcpy(&dynamic_piece->piece, piece, sizeof(piece_t));
  dynamic_piece->lock_delay = 0;
  dynamic_piece->orientation = PIECE_ORIENTATION_0;
  dynamic_piece->position.x = FIELD_WIDTH / 2 - 1;
  dynamic_piece->position.y = FIELD_HEIGHT - 1;
}

uint8_t color_ansi_fg(color_t color) {
  switch (color) {
  case COLOR_ANSI_BLACK:
    return 30;
  case COLOR_ANSI_YELLOW:
    return 33;
  case COLOR_ANSI_BRIGHT_RED:
    return 91;
  case COLOR_ANSI_BRIGHT_GREEN:
    return 92;
  case COLOR_ANSI_BRIGHT_YELLOW:
    return 93;
  case COLOR_ANSI_BRIGHT_BLUE:
    return 94;
  case COLOR_ANSI_BRIGHT_MAGENTA:
    return 95;
  case COLOR_ANSI_BRIGHT_CYAN:
    return 96;
  default:
    return 30;
  }
}

uint8_t color_ansi_bg(color_t color) {
  switch (color) {
  case COLOR_ANSI_BLACK:
    return 40;
  case COLOR_ANSI_YELLOW:
    return 43;
  case COLOR_ANSI_BRIGHT_RED:
    return 101;
  case COLOR_ANSI_BRIGHT_GREEN:
    return 102;
  case COLOR_ANSI_BRIGHT_YELLOW:
    return 103;
  case COLOR_ANSI_BRIGHT_BLUE:
    return 104;
  case COLOR_ANSI_BRIGHT_MAGENTA:
    return 105;
  case COLOR_ANSI_BRIGHT_CYAN:
    return 106;
  default:
    return 40;
  }
}
