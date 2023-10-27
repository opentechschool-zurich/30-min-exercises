#include <iostream>
#include <array>

// 0 0 0 0
// 0 0 0 0
// 0 0 0 0
// 0 0 0 0
// 0 0 0 0
// 0 0 0 0
const int world_n = 4;
const int world_m = 6;

using World = std::array<bool, world_n * world_m>;

// 0 0
// 0 0
// 0 0
const int piece_n = 2;
const int piece_m = 3;

// TODO: if piece would be a vector, we could use different geometries for the pieces...
using Piece = std::array<bool, piece_n * piece_m>;

void display_word(const World& world) {
    for (int j = 0; j < world_m; j++) {
        for (int i = 0; i < world_n; i++) {
            std::cout << world[j * world_n + i] << " ";
        }
        std::cout << "\n";
    }
}

void display_piece(const Piece& piece) {
    for (int j = 0; j < piece_m; j++) {
        for (int i = 0; i < piece_n; i++) {
            std::cout << piece[j * piece_n + i] << " ";
        }
        std::cout << "\n";
    }
}

bool is_piece_free(const World& world, const Piece& piece, const int row) {
    for (int j = 0; j < piece_m; j++) {
        for(int i = 0; i < piece_n; i++){
            if (piece[j * piece_n + i] == 1) {
                if (world[(row + j) * world_n + i] == 1) {
                    return false;
                }
            }
        }
    }
    return true;
}
    
void place_piece(World& world, const int row, const Piece& piece) {
    for (int j = 0; j < piece_m; j++) {
        for (int i = 0; i < piece_n; i++) {
            if (piece[j * piece_n + i] == 1) {
                world[(row + j) * world_n + i] = 1;
            }
        }
    }
}

int main()
{
    Piece l {{ 1, 1, 0, 1, 0, 1}};
    display_piece(l);
    // std::array<bool, 24> matrix {{ 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0}};
    World world;
    std::fill(world.begin(), world.end(), 0);
    display_word(world);
    
    // while (true) {
    for (int a = 0; a < 10; a++) {
        std::cout << "# " << a << "\n";
        bool busy = false;
        int row;
        for (row = 0; row < world_m - piece_m; row++) {
            if (!is_piece_free(world, l, row)) {
                busy = true;
                break;
            }
        }
        if (row == 0) {
            std::cout << "game over\n";
            return 0;
        }
        place_piece(world, busy ? row - 1 : row, l);
        display_word(world);
    }
}
