# largest sum of non-adjacent values
def friends(houses):
    return 0

if __name__ == '__main__':
    assert friends([1, 2, 3, 4]) == 6
    assert friends([4, 3, 2, 1]) == 6
    assert friends([8, 1, 2, 9]) == 17
    assert friends([1, 2, 1]) == 2
    assert friends([4, 5, 2, 3, 7, 9]) == 21
    assert friends([1]) == 1
    assert friends([]) == 0
    assert friends([7, 2, 3, 9, 1, 4]) == 20
