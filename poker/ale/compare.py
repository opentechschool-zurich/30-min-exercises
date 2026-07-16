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

# def get_royal_flush(hand):
#     # TODO: we don't need to check this: it's the straight flush that wins
#     # same color, 10..1
#     return get_straight_flush(hand) and get_high_card(hand) == 14
# 
def get_straight_flush(hand):
    # same color, contiguous numbers
    straight = get_straight(hand)
    flush = get_flush(hand)
    if straight and flush:
        return straight
    return []

def get_four_of_a_kind(hand):
    # four have same number
    quadruples = get_combinations(hand, 4)
    if len(quadruples) == 1:
        return quadruples + get_not_matching(hand, quadruples)
    return []

def get_full_house(hand):
    # three of a kind and a pair
    three = get_three_of_a_kind(hand)
    two = get_pair(hand)
    if three and two:
        return three + two
    return []

def get_flush(hand):
    # all same color
    previous = hand[0][1]
    for _, color in hand[1:]:
        if color != previous:
            return []
    return get_not_matching(hand, [])

def get_straight(hand):
    # contiguous numbers
    previous = hand[0][0]
    for value, _ in hand[1:]:
        if value != previous - 1:
            return []
        previous -= 1
    return get_not_matching(hand, [])

def get_three_of_a_kind(hand):
    triples = get_combinations(hand, 3)
    if len(triples) == 1:
        return triples + get_not_matching(hand, triples)
    return []

def get_two_pairs(hand):
    pairs = get_combinations(hand, 2)
    if len(pairs) == 2:
        return pairs + get_not_matching(hand, pairs)
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
    return pairs

def get_not_matching(hand, removals):
    return [card[0] for card in hand if card[0] not in removals]

def get_pair(hand):
    pairs = get_combinations(hand, 2)
    if len(pairs) == 1:
        return pairs + get_not_matching(hand, pairs)
    return []

def get_high_card(hand):
    return [v for v, t in hand]

def get_sorted_hand(hand):
    return sorted(hand, key=lambda c: c[0], reverse=True)
    

def get_winner(a, b):
    # first sort the hands by value: we rely on it in multiple places
    a.sort(key=lambda c: c[0], reverse=True)
    b.sort(key=lambda c: c[0], reverse=True)

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
    assert(get_high_card(get_sorted_hand(([(2, '♦'), (3, '♥'), (2, '♠'), (4, '♥'), (5, '♠')]))) == [5, 4, 3, 2, 2])
    assert(get_high_card(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (4, '♥'), (5, '♠')])) == [5, 4, 2, 1, 1])
    assert(get_pair(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (4, '♥'), (5, '♠')])) == [1, 5, 4, 2])
    assert(get_pair(get_sorted_hand([(1, '♦'), (3, '♥'), (2, '♠'), (4, '♥'), (5, '♠')])) == [])
    assert(get_two_pairs(get_sorted_hand([(1, '♦'), (3, '♥'), (2, '♠'), (4, '♥'), (5, '♠')])) == [])
    assert(get_two_pairs(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (4, '♥'), (5, '♠')])) == [])
    assert(get_two_pairs(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (5, '♠')])) == [2, 1, 5])
    assert(get_two_pairs(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [])
    assert(get_three_of_a_kind(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [2, 1, 1])
    assert(get_three_of_a_kind(get_sorted_hand([(1, '♦'), (2, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [])
    assert(get_three_of_a_kind(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (5, '♠')])) == [])
    assert(get_straight(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (5, '♠')])) == [])
    assert(get_straight(get_sorted_hand([(2, '♦'), (1, '♥'), (3, '♠'), (4, '♥'), (5, '♠')])) == [5, 4, 3, 2, 1])
    assert(get_flush(get_sorted_hand([(2, '♦'), (1, '♥'), (3, '♠'), (4, '♥'), (5, '♠')])) == [])
    assert(get_flush(get_sorted_hand([(2, '♠'), (1, '♠'), (3, '♠'), (4, '♠'), (6, '♠')])) == [6, 4, 3, 2, 1])
    # print(get_full_house(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])))
    # assert(get_full_house(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [2, 1])
    # assert(get_full_house(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (3, '♠')])) == [])
    # assert(get_full_house(get_sorted_hand([(3, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [])
    assert(get_four_of_a_kind(get_sorted_hand([(1, '♦'), (1, '♥'), (2, '♠'), (2, '♥'), (5, '♠')])) == [])
    assert(get_four_of_a_kind(get_sorted_hand([(1, '♦'), (2, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [2, 1])
    assert(get_straight_flush(get_sorted_hand([(1, '♦'), (2, '♥'), (2, '♠'), (2, '♥'), (2, '♠')])) == [])
    assert(get_straight_flush(get_sorted_hand([(1, '♦'), (2, '♦'), (3, '♦'), (4, '♦'), (5, '♦')])) == [5, 4, 3, 2, 1])

    # deck = get_shuffled_deck()
    # print(len(deck), deck)
    # a, b = get_valid_hands(deck)
    # print('a', a)
    # print('b', b)
    # print(len(deck), deck)

    hand_a = [(1, '♦'), (2, '♥'), (3, '♠'), (5, '♥'), (6, '♠')]
    hand_b = [(1, '♣'), (2, '♣'), (3, '♣'), (4, '♣'), (8, '♣')]
    assert(get_winner(hand_a, hand_b) == 'b')
    hand_a = [(1, '♦'), (1, '♥'), (3, '♠'), (5, '♥'), (6, '♠')]
    hand_b = [(1, '♣'), (2, '♣'), (3, '♣'), (4, '♣'), (8, '♣')]
    assert(get_winner(hand_a, hand_b) == 'a')
    hand_a = [(9, '♦'), (9, '♥'), (3, '♠'), (5, '♥'), (6, '♠')]
    hand_b = [(1, '♣'), (1, '♥'), (3, '♣'), (3, '♥'), (8, '♣')]
    assert(get_winner(hand_a, hand_b) == 'b')
    # hand_a = [(1, '♦'), (2, '♥'), (3, '♠'), (5, '♥'), (8, '♠')]
    # hand_b = [(1, '♣'), (2, '♣'), (3, '♣'), (4, '♣'), (8, '♣')]
    # assert(get_winner(hand_a, hand_b) == 'a')

    # [(1, '♦'), (1, '♥'), (2, '♠'), (3, '♥'), (3, '♠')]
    

if __name__ == '__main__':
    main()
