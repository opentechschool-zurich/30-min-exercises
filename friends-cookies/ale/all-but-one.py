def friends(houses):
    # how many different groups of friends there are? n
    n = len(houses)
    max_amount = 0
    #You checking the houses one by one
    for i in range(0, n):
        amount = 0
    # taking each element to a house 
        for j, cookies in enumerate(houses):
        # js: for ([j, cookies] of houses.entries()) {

            # print(j, cookies)
            if i != j:
                amount = amount + cookies
        max_amount = max(max_amount, amount) 
    return max_amount

# O(n)
def friends2(houses):
    if len(houses) == 0:
        return 0
    return sum(houses) - min(houses)

if __name__ == '__main__':
    assert friends([1, 2, 3, 4]) == 9
    assert friends([4, 2, 9, 8]) == 21
    assert friends([9, 2, 3, 5, 3, 12]) == 32
    assert friends([2, 2, 2]) == 4
    assert friends([1]) == 0
    assert friends([]) == 0
    assert friends2([1, 2, 3, 4]) == 9
    assert friends2([4, 2, 9, 8]) == 21
    assert friends2([9, 2, 3, 5, 3, 12]) == 32
    assert friends2([2, 2, 2]) == 4
    assert friends2([1]) == 0
    assert friends2([]) == 0
