import itertools
import random

def get_shuffled_deck():
   suits = ['♠', '♥', '♦', '♣']
   rank = range(1, 14)
   deck = list(itertools.product(rank, suits))
   random.shuffle(deck)
   return deck

def get_valid_hands(deck):
    a = deck[0:5]
    b = deck[5:10]
    del deck[:10]
    return a, b

# def is_royal_flush(hand):
#     # TODO: we don't need to check this: it's the straight flush that wins
#     # same color, 10..1
#     return is_straight_flush(hand) and get_high_card(hand) == 14
# 
def is_straight_flush(hand):
    # same color, contiguous numbers
    return is_straight(hand) and is_flush(hand)

def is_four_of_a_kind(hand):
    # four have same number
    quadruples = get_combinations(hand, 4)
    if len(quadruples) == 1:
        return True
    return False

def is_full_house(hand):
    # three of a kind and a pair
    return is_three_of_a_kind(hand) and get_pair(hand)

def is_flush(hand):
    # all same color
    previous = hand[0][1]
    for _, color in hand[1:]:
        if color != previous:
            return False
    return True

def is_straight(hand):
    # contiguous numbers
    hand.sort(key=lambda v: v[0])
    previous = hand[0][0]
    for value, _ in hand[1:]:
        if value != previous + 1:
            return False
        previous += 1
    return True

def is_three_of_a_kind(hand):
    triples = get_combinations(hand, 3)
    if len(triples) == 1:
        return True
    return False

def get_two_pairs(hand):
    pairs = get_combinations(hand, 2)
    if len(pairs) == 2:
        return pairs + get_not_matching(sorted(hand), pairs)
    return []

def get_combinations(hand, n):
    combinations = {}
    pairs = []
    for value, color in hand:
        if value in combinations:
            combinations[value] += 1
        else:
            combinations[value] = 1
    for value, count in combinations.items():
        if count == n:
            pairs.append(value)
    return sorted(pairs, reverse=True)

def get_not_matching(hand, removals):
    return [card for card in hand if card not in removals]

def get_pair(hand):
    # TODO: if same pair, then high card with the rest
    pairs = get_combinations(hand, 2)
    if len(pairs) == 1:
        return pairs + get_not_matching(sorted(hand, reverse=True), pairs)
    return []

def get_high_card(hand):
    # TODO: the high card could be the same for both, than take the second best
    # high = 0
    # for card in hand:
    #     if card[0] == 1:
    #         return 14
    #     if card[0] > high:
    #         high = card[0]
    # return high
    return sorted([v for v, t in hand], reverse=True)
    

def get_winner(a, b):
    # TODO: we could sort the hands at the beginning of the checking and all the list are then naturally sorted
    # a.sort()
    # b.sort()

    score_a = get_two_pairs(a)
    score_b = get_two_pairs(b)
    if score_a or score_b:
        return 'a' if score_a > score_b else 'b'
    score_a = get_pair(a)
    score_b = get_pair(b)
    if score_a or score_b:
        return 'a' if score_a > score_b else 'b'
    score_a = get_high_card(a)
    score_b = get_high_card(b)
    if score_a > score_b:
        return 'a'
    elif score_a < score_b:
        return 'b'
    else:
        return None
    

def main():
    colors = ['D', 'H', 'C', 'S']
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    hand_a = [(1, 'D'), (1, 'H'), (1, 'S'), (3, 'H'), (3, 'S')]
    hand_b = [(1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C')]
    # print(get_winner(hand_a, hand_b))

    # assert(get_high_card([(2, 'D'), (3, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == 5)
    # assert(get_high_card([(1, 'D'), (1, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == 14)
    # assert(is_pair([(1, 'D'), (1, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == True)
    # assert(is_pair([(1, 'D'), (3, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == False)
    # assert(is_two_pairs([(1, 'D'), (3, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == False)
    # assert(is_two_pairs([(1, 'D'), (1, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == False)
    # assert(is_two_pairs([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == True)
    # assert(is_two_pairs([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    # assert(is_three_of_a_kind([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == True)
    # assert(is_three_of_a_kind([(1, 'D'), (2, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    # assert(is_three_of_a_kind([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == False)
    # assert(is_straight([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == False)
    # assert(is_straight([(2, 'D'), (1, 'H'), (3, 'S'), (4, 'H'), (5, 'S')]) == True)
    # assert(is_flush([(2, 'D'), (1, 'H'), (3, 'S'), (4, 'H'), (5, 'S')]) == False)
    # assert(is_flush([(2, 'S'), (1, 'S'), (3, 'S'), (4, 'S'), (5, 'S')]) == True)
    # assert(is_full_house([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == True)
    # assert(is_full_house([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (3, 'S')]) == False)
    # assert(is_full_house([(3, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    # assert(is_four_of_a_kind([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == False)
    # assert(is_four_of_a_kind([(1, 'D'), (2, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == True)
    # assert(is_straight_flush([(1, 'D'), (2, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    # assert(is_straight_flush([(1, 'D'), (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D')]) == True)

    # deck = get_shuffled_deck()
    # print(len(deck), deck)
    # a, b = get_valid_hands(deck)
    # print('a', a)
    # print('b', b)
    # print(len(deck), deck)

    hand_a = [(1, 'D'), (2, 'H'), (3, 'S'), (5, 'H'), (6, 'S')]
    hand_b = [(1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (8, 'C')]
    assert(get_winner(hand_a, hand_b) == 'b')
    hand_a = [(1, 'D'), (1, 'H'), (3, 'S'), (5, 'H'), (6, 'S')]
    hand_b = [(1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (8, 'C')]
    assert(get_winner(hand_a, hand_b) == 'a')
    hand_a = [(9, 'D'), (9, 'H'), (3, 'S'), (5, 'H'), (6, 'S')]
    hand_b = [(1, 'C'), (1, 'H'), (3, 'C'), (3, 'H'), (8, 'C')]
    assert(get_winner(hand_a, hand_b) == 'b')
    # hand_a = [(1, 'D'), (2, 'H'), (3, 'S'), (5, 'H'), (8, 'S')]
    # hand_b = [(1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (8, 'C')]
    # assert(get_winner(hand_a, hand_b) == 'a')

    # [(1, 'D'), (1, 'H'), (2, 'S'), (3, 'H'), (3, 'S')]
    

if __name__ == '__main__':
    main()
