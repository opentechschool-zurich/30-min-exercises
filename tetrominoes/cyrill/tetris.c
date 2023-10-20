#include <curses.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// TODO better ui (piece preview, center field, handle term too small)
//   TODO draw ghost (bright black)
// TODO hold
// TODO pause
// TODO high-score
// TODO menu
// TODO special point counts (combo, t-spin, back-to-back action)
// TODO start-level
// TODO b-type

#define FIELD_WIDTH 10
#define FIELD_HEIGHT 20

const uint8_t STDIN = 0;

const uint8_t LOCK_DELAY = 30; // frames

const uint8_t FPS = 60;

const char UTF8_LOWER_HALF_BLOCK[] = {0xe2, 0x96, 0x84, 0x00};
const char UTF8_BOX_DRAWINGS_LIGHT_VERTICAL[] = {0xe2, 0x94, 0x82, 0x00};
const char UTF8_BOX_DRAWINGS_LIGHT_HORIZONTAL[] = {0xe2, 0x94, 0x80, 0x00};
const char UTF8_BOX_DRAWINGS_ARC_UP_AND_RIGHT[] = {0xe2, 0x95, 0xb0, 0x00};
const char UTF8_BOX_DRAWINGS_ARC_UP_AND_LEFT[] = {0xe2, 0x95, 0xaf, 0x00};

typedef uint8_t bool_t;

typedef enum color {
  COLOR_ANSI_BLACK,
  COLOR_ANSI_YELLOW,
  COLOR_ANSI_WHITE,
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

const piece_t *PIECES[7] = {&I, &J, &L, &O, &S, &T, &Z};

typedef struct rng {
  int data;
  uint8_t remaining;
} rng_t;

void rng_init(rng_t *rng);
uint8_t rng_next(rng_t *rng, uint8_t max);
void rng_shuffle(rng_t *rng, void **data, uint8_t length);

typedef struct pieces_buffer {
  rng_t rng;
  uint8_t cursor;
  piece_t *pieces[14];
} pieces_buffer_t;

void pieces_buffer_init(pieces_buffer_t *pieces_buffer);
piece_t *pieces_buffer_pop(pieces_buffer_t *pieces_buffer);

typedef struct dynamic_piece {
  piece_orientation_t orientation;
  vec2_t position;
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
  uint32_t score;
  uint8_t lines;
  uint8_t level;
  uint8_t fall_delay;
  uint8_t lock_delay;
  frame_timer_t frame_timer;
  dynamic_piece_t dynamic_piece;
  color_t field[FIELD_HEIGHT][FIELD_WIDTH];
  pieces_buffer_t pieces_buffer;
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

void game_score_line_clears(game_t *game, uint8_t line_clears);

uint8_t speed(uint8_t level);

uint8_t level(uint8_t lines);

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
  game.fall_delay = speed(game.level);

  while (true) { // game loop
    if (frame_timer_tick(&game.frame_timer)) {
      if (game.fall_delay > 0) {
        game.fall_delay--;
      } else {
        game.fall_delay = speed(game.level);
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
  pieces_buffer_init(&game->pieces_buffer);
  const piece_t *first_piece = pieces_buffer_pop(&game->pieces_buffer);
  dynamic_piece_init(&game->dynamic_piece, first_piece);
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
  const vec2_t field_offset = {2, 1};
  for (uint8_t y = 0; y < FIELD_HEIGHT; y += 2) {
    for (uint8_t x = 0; x < FIELD_WIDTH; x++) {
      printf("\033[%d;%df\033[%d;%dm%s", y / 2 + field_offset.y,
             x + field_offset.x, color_ansi_fg(field_buffer[y + 1][x]),
             color_ansi_bg(field_buffer[y][x]), UTF8_LOWER_HALF_BLOCK);
    }
  }

  // border
  printf("\033[%d;%dm", color_ansi_fg(COLOR_ANSI_WHITE),
         color_ansi_bg(COLOR_ANSI_BLACK));
  for (uint8_t y = 0; y < FIELD_HEIGHT / 2; y++) {
    printf("\033[%d;%df%s\033[%d;%df%s", y + field_offset.y, field_offset.x - 1,
           UTF8_BOX_DRAWINGS_LIGHT_VERTICAL, y + field_offset.y,
           field_offset.x + FIELD_WIDTH, UTF8_BOX_DRAWINGS_LIGHT_VERTICAL);
  }
  printf("\033[%d;%df%s", field_offset.y + FIELD_HEIGHT / 2, field_offset.x - 1,
         UTF8_BOX_DRAWINGS_ARC_UP_AND_RIGHT);
  for (uint8_t i = 0; i < FIELD_WIDTH; i++) {
    printf("%s", UTF8_BOX_DRAWINGS_LIGHT_HORIZONTAL);
  }
  printf("%s", UTF8_BOX_DRAWINGS_ARC_UP_AND_LEFT);

  // score
  printf("\033[%d;%df%s", field_offset.y, field_offset.x + FIELD_WIDTH + 2, "score");
  printf("\033[%d;%df%5d", field_offset.y + 1, field_offset.x + FIELD_WIDTH + 2, game->score);
  printf("\033[%d;%df%s", field_offset.y + 3, field_offset.x + FIELD_WIDTH + 2, "level");
  printf("\033[%d;%df%5d", field_offset.y + 4, field_offset.x + FIELD_WIDTH + 2, game->level);
  printf("\033[%d;%df%s", field_offset.y + 6, field_offset.x + FIELD_WIDTH + 2, "lines");
  printf("\033[%d;%df%5d", field_offset.y + 7, field_offset.x + FIELD_WIDTH + 2, game->lines);
}

void game_handle_input(game_t *game) {
  switch (getch()) {
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
    while (!game_fall(game))
      game->score += 2;
    break;
  case KEY_DOWN:
  case 'j':
    game_fall(game);
    game->score++;
    break;
  default:
    break;
  }
}

void game_rotate_right(game_t *game) {
  dynamic_piece_t rotated = game->dynamic_piece;
  vec2_rotate_right(4, rotated.piece.tiles);
  rotated.orientation = (rotated.orientation + 1) % 4;
  if (game_adjust_placement(game, &rotated)) {
    game->dynamic_piece = rotated;
    game->fall_delay = LOCK_DELAY;
  }
}

void game_rotate_left(game_t *game) {
  dynamic_piece_t rotated = game->dynamic_piece;
  vec2_rotate_left(4, rotated.piece.tiles);
  rotated.orientation = (rotated.orientation + 3) % 4;
  if (game_adjust_placement(game, &rotated)) {
    game->dynamic_piece = rotated;
    game->fall_delay = LOCK_DELAY;
  }
}

void game_shift_right(game_t *game) {
  dynamic_piece_t shifted = game->dynamic_piece;
  shifted.position.x++;
  if (!game_check_collision(game, &shifted)) {
    game->dynamic_piece = shifted;
    game->fall_delay = LOCK_DELAY;
  }
}

void game_shift_left(game_t *game) {
  dynamic_piece_t shifted = game->dynamic_piece;
  shifted.position.x--;
  if (!game_check_collision(game, &shifted)) {
    game->dynamic_piece = shifted;
    game->fall_delay = LOCK_DELAY;
  }
}

bool_t game_fall(game_t *game) {
  dynamic_piece_t shifted = game->dynamic_piece;
  shifted.position.y--;
  if (game_check_collision(game, &shifted)) {
    if (game->lock_delay != 0) {
      game->fall_delay = game->lock_delay;
      game->lock_delay = 0;
      return 0;
    }
    const vec2_t position = game->dynamic_piece.position;
    const piece_t *piece = &game->dynamic_piece.piece;
    for (uint8_t i = 0; i < 4; i++) {
      const vec2_t screen_position = {.x = position.x + piece->tiles[i].x,
                                      .y = FIELD_HEIGHT -
                                           (position.y + piece->tiles[i].y)};
      game->field[screen_position.y][screen_position.x] = piece->color;
    }
    game_remove_full_lines(game);
    const piece_t *next_piece = pieces_buffer_pop(&game->pieces_buffer);
    dynamic_piece_init(&game->dynamic_piece, next_piece);
    if (game_check_collision(game, &game->dynamic_piece)) {
      // TODO handle end of game
      curs_set(2);
      endwin();
      printf("\033[2J\033[1;1f\033[31;40mYou lose!\nscore: %d\n", game->score);
      exit(0);
    }
    game->fall_delay = speed(game->level);
    game->lock_delay =
        game->fall_delay > LOCK_DELAY ? 0 : LOCK_DELAY - game->fall_delay;
    return 1;
  } else {
    game->dynamic_piece.position.y--;
    return 0;
  }
}

void game_remove_full_lines(game_t *game) {
  uint8_t line_clears = 0;
  for (uint8_t y = FIELD_HEIGHT - 1; y >> 0; y--) {
    bool_t line_full = 1;
    for (uint8_t x = 0; x < FIELD_WIDTH; x++) {
      if (game->field[y][x] == 0) {
        line_full = 0;
        break;
      }
    }
    if (line_full) {
      line_clears++;
      memmove(&game->field[1], game->field, y * FIELD_WIDTH * sizeof(color_t));
      y++;
    }
  }
  game_score_line_clears(game, line_clears);
  game->lines += line_clears;
  game->level = level(game->lines);
}

bool_t game_adjust_placement(game_t *game, dynamic_piece_t *dynamic_piece) {
  const vec2_t position = dynamic_piece->position;
  const vec2_t(*offsets)[4][5] = dynamic_piece->piece.offsets;
  const vec2_t(*from_offsets)[5] = &(*offsets)[game->dynamic_piece.orientation];
  const vec2_t(*to_offsets)[5] = &(*offsets)[dynamic_piece->orientation];
  for (uint8_t i = 0; i < 5; i++) {
    dynamic_piece->position.x =
        position.x + ((*from_offsets)[i].x - (*to_offsets)[i].x);
    dynamic_piece->position.y =
        position.y + ((*from_offsets)[i].y - (*to_offsets)[i].y);
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

void game_score_line_clears(game_t *game, uint8_t line_clears) {
  uint32_t points = 0;
  switch (line_clears) {
  case 1:
    points = 100;
    break;
  case 2:
    points = 300;
    break;
  case 3:
    points = 500;
    break;
  case 4:
    points = 800;
    break;
  default:
    points = 0;
    break;
  }
  game->score += points * (game->level + 1);
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

void rng_init(rng_t *rng) {
  // seed rng with epoch seconds
  srand(time(NULL));
  rng->remaining = 0;
}

uint8_t rng_next(rng_t *rng, uint8_t max) {
  uint8_t result = max + 1, bits = 0, mask = max;
  // count how many bits are needed to represent max (log2)
  while (mask >>= 1)
    bits++;
  mask = (1 << bits) - 1;
  // We reject random numbers > n this should give us uniformly distributed
  // random numbers in the range 0..max.
  // In 1/(max + 1) cases we will "waste" a number.
  while (result > max) {
    if (rng->remaining < bits) {
      rng->remaining = sizeof(rng->data) * 8;
      rng->data = rand();
    }
    result = rng->data & mask;
    rng->data >>= bits;
    rng->remaining -= bits;
  }
  return result;
}

// fisher-yates shuffle
void rng_shuffle(rng_t *rng, void **data, uint8_t length) {
  for (uint8_t i = 0; i < length - 1; i++) {
    const uint8_t j = i + rng_next(rng, length - i - 1);
    void *t = data[i];
    data[i] = data[j];
    data[j] = t;
  }
}

void pieces_buffer_init(pieces_buffer_t *pieces_buffer) {
  pieces_buffer->cursor = 0;
  rng_init(&pieces_buffer->rng);
  memcpy(pieces_buffer->pieces, PIECES, 7 * sizeof(piece_t *));
  memcpy(&pieces_buffer->pieces[7], PIECES, 7 * sizeof(piece_t *));
  rng_shuffle(&pieces_buffer->rng, (void **)pieces_buffer->pieces, 7);
  rng_shuffle(&pieces_buffer->rng, (void **)&pieces_buffer->pieces[7], 7);
}

piece_t *pieces_buffer_pop(pieces_buffer_t *pieces_buffer) {
  piece_t *result = pieces_buffer->pieces[pieces_buffer->cursor];
  pieces_buffer->cursor = (pieces_buffer->cursor + 1) % 14;
  if (pieces_buffer->cursor % 7 == 0) {
    const uint8_t i = (pieces_buffer->cursor + 7) % 14;
    memcpy(&pieces_buffer->pieces[i], PIECES, 7 * sizeof(piece_t *));
    rng_shuffle(&pieces_buffer->rng, (void **)&pieces_buffer->pieces[i], 7);
  }
  return result;
}

void dynamic_piece_init(dynamic_piece_t *dynamic_piece, const piece_t *piece) {
  memcpy(&dynamic_piece->piece, piece, sizeof(piece_t));
  dynamic_piece->orientation = PIECE_ORIENTATION_0;
  dynamic_piece->position.x = FIELD_WIDTH / 2 - 1;
  dynamic_piece->position.y = FIELD_HEIGHT - 1;
}

uint8_t speed(uint8_t level) {
  switch (level) {
  case 0:
    return 48;
  case 1:
    return 43;
  case 2:
    return 38;
  case 3:
    return 33;
  case 4:
    return 28;
  case 5:
    return 23;
  case 6:
    return 18;
  case 7:
    return 13;
  case 8:
    return 8;
  case 9:
    return 6;
  case 10:
  case 11:
  case 12:
    return 5;
  case 13:
  case 14:
  case 15:
    return 4;
  case 16:
  case 17:
  case 18:
    return 3;
  case 19:
  case 21:
  case 22:
  case 23:
  case 24:
  case 25:
  case 26:
  case 27:
  case 28:
    return 2;
  default:
    return 1;
  }
}

uint8_t level(uint8_t lines) {
  return lines / 10;
}

uint8_t color_ansi_fg(color_t color) {
  switch (color) {
  case COLOR_ANSI_BLACK:
    return 30;
  case COLOR_ANSI_YELLOW:
    return 33;
  case COLOR_ANSI_WHITE:
    return 37;
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
  case COLOR_ANSI_WHITE:
    return 47;
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
