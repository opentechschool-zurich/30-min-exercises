import itertools

def calcolo_enigmatico(calcolo):
    # unique letters in the calculation
    letters = set(''.join([calcolo[i][j] for i in [0, 2, 3] for j in [0, 2, 3]]))
    # a number cannot start with the 0 digit
    not_0 = set([calcolo[i][j][0] for i in [0, 2, 3] for j in [0, 2, 3]])
    n = len(letters)
    digits = range(10)
    # try each permutation of the 10 digits for the n defined characters
    for permutation in itertools.permutations(digits, n):
        # a cipher carries the attribution of the digits to the letters
        cipher = {}
        for c, d in zip(letters, permutation):
            cipher[c]  = d
        # if the calculation with the current cipher matches
        if not calculate(calcolo, cipher, not_0):
            continue
        # ... we have found the right matches!
        print_result(calcolo, cipher, permutation)

def calculate(calcolo, cipher, not_0):
    if any(cipher[c] == 0 for c in not_0):
        return False
    for row in [0, 2, 3]:
        if not calculate_row(calcolo[row], cipher):
            return False
    for i in [0, 2, 3]:
        column = [row[i] for row in calcolo]
        if not calculate_row(column, cipher):
            return False
    return True

def calculate_row(row, cipher):
    a = string_to_num(row[0], cipher)
    b = string_to_num(row[2], cipher)
    c = string_to_num(row[3], cipher)
    match row[1]:
        case '*':
            return a * b == c
        case '+':
            return a + b == c
        case '-':
            return a - b == c
        case '/':
            return a // b == c

def string_to_num(a, cipher):
    num_a = 0
    for c in a:
        num_a *= 10
        num_a += cipher[c]
    return num_a

def print_result(calcolo, cipher, permutation):
    result = [['', '', '', ''] for i in calcolo]
    max_length = 0
    for row in [0, 2, 3]:
        for column in [0, 2, 3]:
            result[column][row] = string_to_num(calcolo[column][row], cipher)
            max_length = max(max_length, len(calcolo[column][row]))
    for column in range(len(calcolo[0])):
        result[1][column] = calcolo[1][column]
    for row in range(len(calcolo)):
        result[row][1] = calcolo[row][1]
    for row in result:
        for i, field in enumerate(row):
            if i == 1:
                print(f' {field.rjust(1)} ', end='')
            else:
                print(' ' + str(field).rjust(max_length) + ' ', end='')
        print()

def main():
    calcolo = [
        ['ab',  '*',  'c',  'ade'],  
        ['*',    '',  '*',    '*'],  
        ['af',  '*',  'b',   'bg'],  
        ['ahg', '*', 'ae', 'bede'],
    ]

    calcolo_enigmatico(calcolo)

if __name__ == '__main__':
    main()
