#!/usr/bin/env python3

def compute_change(register, amount):
    """
    Compute minimal `denominations` and counts to represent the given `amount`.

    Returns `None` if no solution was found.
    """
    result = {}
    rest = amount
    for denomination in sorted(register.keys(), reverse = True):
        count = rest // denomination        
        if count > register[denomination]:
            count = register[denomination]
        rest = rest - denomination * count
        if count > 0:
            result[denomination] = count

    if rest == 0:
        return result
    else:
        return None

if __name__ == '__main__':
    assert(compute_change({5: 3, 2: 5}, 8) == None)
    assert(compute_change({5: 1, 2: 1, 1: 2}, 8) == {5: 1, 2: 1, 1: 1})
    assert(compute_change({5: 1, 2: 1, 1: 2}, 9) == {5: 1, 2: 1, 1: 2})
    assert(compute_change({}, 0) == {})
    assert(compute_change({3: 1, 2: 5, 1: 6}, 0) == {})
