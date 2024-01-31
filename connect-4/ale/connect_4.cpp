#include <iostream>
#include <array>
#include <cassert>
#include <algorithm>

const int COLUMNS = 7;
const int ROWS = 6;
using Board = std::array<std::array<int, COLUMNS>, ROWS>;

void display(const Board& board) {
    std::cout << "-----\n";
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLUMNS; j++) {
            std::cout << board[i][j];
        }
        std::cout << "\n";
    }
}

int drop(int column, int player, Board& board) {
    for (int i = 0; i < ROWS; i++) {
        if (board.at(i).at(column) == 0) {
            board.at(i).at(column) = player;
            return i;
        }
    }
    return -1;
}

bool is_full(const Board& board) {
    for (int j = 0; j < COLUMNS; j++) {
        if (board[ROWS - 1][j] == 0) {
            return false;
        }
    }
    return true;
}

bool has_winner(int row, int column, const Board& board) {
    int player = board[row][column];
    // check vertical
    int counter = 1;
    for (int j = row - 1; j >= 0; j--) {
        if (board.at(j).at(column) == player) {
            counter += 1;
        } else {
            break;
        }
        if (counter == 4) {
            return true;
        }
    }
    // horizontal
    counter = 0;
    for (int j = 0; j < COLUMNS; j++) {
        if (board.at(row).at(j) == player) {
            counter += 1;
        } else {
            counter = 0;
        }
        if (counter == 4) {
            return true;
        }
    }
    // tl-br diagonal
    counter = 0;
    for (int i = std::max(0, row - column), j = std::max(0, column - row); i < ROWS && j < COLUMNS; i++, j++) {
        if (board.at(i).at(j) == player) {
            counter += 1;
        } else {
            counter = 0;
        }
        if (counter == 4) {
            return true;
        }
    }
    // bl-tr diagonal
    counter = 0;
    for (int i = std::max(0, row + column - ROWS), j = std::min(COLUMNS - 1, column + row); i < ROWS && j >= 0 ; i++, j--) {
        if (board.at(i).at(j) == player) {
            counter += 1;
        } else {
            counter = 0;
        }
        if (counter == 4) {
            return true;
        }
    }
    return false;
}

// 3, 2; 5, 2

//  [0, 0, 0, 0, 0, 0, 0], // bottom
//  [0, 0, 0, 0, 0, 0, 0],
//  [0, 0, 0, 1, 0, 0, 0],
//  [0, 0, 0, 0, 0, 0, 0],
//  [0, 0, 0, 0, 0, 0, 0],
//  [0, 0, 0, 0, 0, 0, 0], // top


void test() {
    {
        Board board{};
        int player = 1;
        drop(2, player, board);
        drop(2, player, board);
        int row = drop(2, player, board);
        assert(has_winner(row, 2, board) == false);
        row = drop(2, player, board);
        display(board);
        assert(has_winner(row, 2, board) == true);
    }
    {
        Board board{};
        int player = 1;
        drop(1, player, board);
        drop(2, player, board);
        int row = drop(3, player, board);
        assert(has_winner(row, 3, board) == false);
        row = drop(4, player, board);
        display(board);
        assert(has_winner(row, 4, board) == true);
    }
    {
        // 0100000
        // 0010000
        // 0001000
        // 0000100
        // 0000000
        // 0000000
        Board board{};
        int player = 1;
        board[0][1] = 1;
        board[1][2] = 1;
        board[2][3] = 1;
        display(board);
        assert(has_winner(2, 3, board) == false);
        board[3][4] = 1;
        // display(board);
        assert(has_winner(3, 4, board) == true);
    }
    {
        // 0000000
        // 0000000
        // 0000001
        // 0000010
        // 0000100
        // 0001000
        Board board{};
        board[2][COLUMNS - 1] = 1;
        board[3][COLUMNS - 2] = 1;
        board[4][COLUMNS - 3] = 1;
        assert(has_winner(4, COLUMNS - 3, board) == false);
        board[5][COLUMNS - 4] = 1;
        assert(has_winner(5, COLUMNS - 3, board) == true);
        // display(board);
    }
    {
        // 0000010
        // 0000100
        // 0001000
        // 0010000
        // 0000000
        // 0000000
        Board board{};
        board[0][COLUMNS - 2] = 1;
        board[1][COLUMNS - 3] = 1;
        board[2][COLUMNS - 4] = 1;
        assert(has_winner(2, COLUMNS - 4, board) == false);
        board[3][COLUMNS - 5] = 1;
        // display(board);
        assert(has_winner(3, COLUMNS - 5, board) == true);
    }
}

int main()
{
    // test();
    Board board{};
    int player = 1;
    int column;
    while (!is_full(board)) {
        display(board);
        std::cout << "Player " << player << ": ";
        std::cin >> column;
        if (column < 0 || column > COLUMNS - 1) {
            continue;
        }
        int row = drop(column, player, board);
        if (row == -1) {
            continue;
        }
        if (has_winner(row, column, board)) {
            std::cout << "Player " << player << " has won.\n";
            display(board);
            break;
        }
        player = player == 1 ? 2 : 1;
    }
}
