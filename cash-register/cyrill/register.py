#!/usr/bin/env python3

import greedy_ukp
import greedy_bkp
import greedy_with_backtracking_bkp

def display_result(result):
    if result == None:
        print('  no solution')
        return
    for denomination in sorted(result.keys(), reverse = True):
        print('  {:3} × {:3}'.format(denomination, result[denomination]))

def register():
    denominations = input('denominations (separated by spaces): ').split(' ')
    denominations = filter(lambda s: s != '', denominations)
    denominations = map(lambda s: int(s), denominations)
    denominations = list(denominations)

    register = {}
    for denomination in denominations:
        count = int(input('count of {}s: '.format(denomination)))
        register[denomination] = count

    amount = int(input('amount: '))

    result_greedy_ukp = greedy_ukp.compute_change(denominations, amount)
    print("\nresult greedy UKP:")
    display_result(result_greedy_ukp)

    result_greedy_bkp = greedy_bkp.compute_change(register, amount)
    print("\nresult greedy BKP:")
    display_result(result_greedy_bkp)

    result_greedy_with_backtracking_bkp = greedy_with_backtracking_bkp.compute_change(register, amount)
    print("\nresult greedy with backtracking BKP:")
    display_result(result_greedy_with_backtracking_bkp)

if __name__ == '__main__':
    try:
        register()
    except KeyboardInterrupt:
        print('\nbye')
