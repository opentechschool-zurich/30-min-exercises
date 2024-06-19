// I-IIXIIXIIXIIXIIX

#include <cassert>

int count(int money, int price) {
    int count = money / price;
    return count > 1
        ? count + (count - 1) / 2
        : count;
}

int main() {
    assert(count(3, 3) == 1);
}
