import itertools
def brute_force(houses):
    n = len(houses)
    max_amount = 0
    house_numbers = range(0, n)
    for i in range(0, n):
        for combination in itertools.combinations(house_numbers, i + 1):
            # check if the previous is -1
            previous = None
            neighbour = False
            for c in combination:
                if previous is not None and c == previous + 1:
                    neighbour = True
                    break
                previous = c
            if neighbour is True:
                continue
            # print('===', combination)
            max_amount = max(max_amount, sum(houses[j] for j in combination))
    return max_amount

if __name__ == '__main__':
    assert brute_force([1, 2, 3, 4]) == 6
    assert brute_force([4, 3, 2, 1]) == 6
    assert brute_force([8, 1, 2, 9]) == 17
    assert brute_force([1, 2, 1]) == 2
    assert brute_force([4, 5, 2, 3, 7, 9]) == 17 # 21?
    assert brute_force([1]) == 1
    assert brute_force([]) == 0
    assert brute_force([7, 2, 3, 9, 1, 4]) == 20
