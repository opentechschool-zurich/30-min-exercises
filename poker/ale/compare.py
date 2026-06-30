def is_royal_flush(hand):
    # TODO: we don't need to check this: it's the straight flush that wins
    # same color, 10..1
    return is_straight_flush(hand) and get_high_card(hand) == 14

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
    return is_three_of_a_kind(hand) and is_pair(hand)

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

def is_two_pairs(hand):
    pairs = get_combinations(hand, 2)
    if len(pairs) == 2:
        return True
    return False

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

def is_pair(hand):
    pairs = get_combinations(hand, 2)
    if len(pairs) == 1:
        return True
    return False

def get_high_card(hand):
    high = 0
    for card in hand:
        if card[0] == 1:
            return 14
        if card[0] > high:
            high = card[0]
    return high

def get_winner(a, b):
    ...
    

def main():
    colors = ['D', 'H', 'C', 'S']
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    hand_a = [(1, 'D'), (1, 'H'), (1, 'S'), (3, 'H'), (3, 'S')]
    hand_b = [(1, 'C'), (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C')]
    # print(get_winner(hand_a, hand_b))

    assert(get_high_card([(2, 'D'), (3, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == 5)
    assert(get_high_card([(1, 'D'), (1, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == 14)
    assert(is_pair([(1, 'D'), (1, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == True)
    assert(is_pair([(1, 'D'), (3, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == False)
    assert(is_two_pairs([(1, 'D'), (3, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == False)
    assert(is_two_pairs([(1, 'D'), (1, 'H'), (2, 'S'), (4, 'H'), (5, 'S')]) == False)
    assert(is_two_pairs([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == True)
    assert(is_two_pairs([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    assert(is_three_of_a_kind([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == True)
    assert(is_three_of_a_kind([(1, 'D'), (2, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    assert(is_three_of_a_kind([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == False)
    assert(is_straight([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == False)
    assert(is_straight([(2, 'D'), (1, 'H'), (3, 'S'), (4, 'H'), (5, 'S')]) == True)
    assert(is_flush([(2, 'D'), (1, 'H'), (3, 'S'), (4, 'H'), (5, 'S')]) == False)
    assert(is_flush([(2, 'S'), (1, 'S'), (3, 'S'), (4, 'S'), (5, 'S')]) == True)
    assert(is_full_house([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == True)
    assert(is_full_house([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (3, 'S')]) == False)
    assert(is_full_house([(3, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    assert(is_four_of_a_kind([(1, 'D'), (1, 'H'), (2, 'S'), (2, 'H'), (5, 'S')]) == False)
    assert(is_four_of_a_kind([(1, 'D'), (2, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == True)
    assert(is_straight_flush([(1, 'D'), (2, 'H'), (2, 'S'), (2, 'H'), (2, 'S')]) == False)
    assert(is_straight_flush([(1, 'D'), (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D')]) == True)

    # [(1, 'D'), (1, 'H'), (2, 'S'), (3, 'H'), (3, 'S')]
    

if __name__ == '__main__':
    main()
