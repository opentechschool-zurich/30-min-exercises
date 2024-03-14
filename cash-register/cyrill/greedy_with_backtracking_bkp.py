#!/usr/bin/env python3

def compute_change(register, amount):
    """
    Compute minimal `denominations` and counts to represent the given `amount`.

    Returns `None` if no solution was found.
    """
    if amount == 0:
        return {}
    
    for denomination in sorted(register.keys(), reverse = True):
        if register[denomination] < 1 or denomination > amount:
            continue
        register = register.copy()
        register[denomination] -= 1
        rest = amount - denomination
        if rest == 0:
            result = {}
            result[denomination] = 1
            return result
        result = compute_change(register, rest)
        if result == None:
            continue
        if denomination in result:
            result[denomination] += 1
        else:
            result[denomination] = 1
        return result
    
    return None

if __name__ == '__main__':
    assert(compute_change({5: 3, 2: 5}, 8) == {2: 4})
    assert(compute_change({5: 3, 2: 5}, 13) == {5: 1, 2: 4})
    assert(compute_change({5: 1, 2: 1, 1: 2}, 8) == {5: 1, 2: 1, 1: 1})
    assert(compute_change({5: 1, 2: 1, 1: 2}, 9) == {5: 1, 2: 1, 1: 2})
    assert(compute_change({}, 0) == {})
    assert(compute_change({3: 1, 2: 5, 1: 6}, 0) == {})
