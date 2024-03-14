#!/usr/bin/env python3

def compute_change(denominations, amount):
    """
    Compute minimal `denominations` and counts to represent the given `amount`.

    Returns `None` if no solution was found.
    """
    denominations = sorted(denominations, reverse = True)

    result = {}
    rest = amount
    for denomination in denominations:
        count = rest // denomination        
        rest = rest % denomination
        if count > 0:
            result[denomination] = count

    if rest == 0:
        return result
    else:
        return None

if __name__ == '__main__':
    assert(compute_change([5, 2], 8) == None)
    assert(compute_change([5, 2, 1], 8) == {5: 1, 2: 1, 1: 1})
    assert(compute_change([5, 2, 1], 9) == {5: 1, 2: 2})
    assert(compute_change([], 0) == {})
    assert(compute_change([3, 2, 1], 0) == {})
