# Write a program that outputs all possibilities to put + or - or nothing
# between the numbers 1,2,…,9 (in this order) such that the result is 100.
#
# For example 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100.

import itertools

def solve():
    digits = [str(i) for i in range(1, 10)]
    operators = ['+', '-', '']

    for combination in itertools.product(operators, repeat=len(digits) - 1):
        calculation = ''
        result = 0
        term = '+'
        for d, o in zip(digits, ('', *combination)):
            calculation += o + d
            if o != '':
                result += int(term)
                term = ''
            term += o + d
        result += int(term)
        if result == 100:
            print(calculation, result)

def solve_with_eval():
    digits = [str(i) for i in range(1, 10)]
    operators = ['+', '-', '']

    for combination in itertools.product(operators, repeat=len(digits) - 1):
        calculation = ''
        for d, o in zip(digits, ('', *combination)):
            calculation += o + d
        if eval(calculation) == 100:
           print(calculation, eval(calculation))

def main():
    solve_with_eval()
    print('---')
    solve()

if __name__ == '__main__':
    main()

# 1+2+3-4+5+6+78+9 100
# 1+2+34-5+67-8+9 100
# 1+23-4+5+6+78-9 100
# 1+23-4+56+7+8+9 100
# 12+3+4+5-6-7+89 100
# 12+3-4+5+67+8+9 100
# 12-3-4+5-6+7+89 100
# 123+4-5+67-89 100
# 123+45-67+8-9 100
# 123-4-5-6-7+8-9 100
# 123-45-67+89 100
