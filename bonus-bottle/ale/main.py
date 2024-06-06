def count_gazzosa(money):
    unit_cost = 3
    amount = money // unit_cost

    bottles = amount

    while bottles >= 3:
        amount += bottles // 3
        bottles = bottles // 3 + bottles % 3
    
    return amount

assert count_gazzosa(3) == 1
assert count_gazzosa(9) == 4
assert count_gazzosa(30) == 14
