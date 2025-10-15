import itertools

#  SEND +
#  MORE =
# -----
# MONEY

def calculate(a, b, c):
    letters = set(a + b + c)
    print(letters)
    ...

def string_to_num(a, cipher):
    num_a = 0
    for c in a:
        num_a *= 10
        num_a += cipher[c]
    return num_a

def calculate_permutations(term_a, term_b, result_c):
    letters = set(term_a + term_b + result_c)
    not_0 = set(term_a[0] + term_b[0] + result_c[0])
    n = len(letters)
    digits = range(10)
    for p in itertools.permutations(digits, n):
        cipher = {}
        for c, d in zip(letters, p):
            cipher[c]  = d
        if any(cipher[c] == 0 for c in not_0):
            continue
        #print(p, cipher)
        num_a = string_to_num(term_a, cipher)
        num_b = string_to_num(term_b, cipher)
        num_c = string_to_num(result_c, cipher)
        if num_a + num_b == num_c:
            print(f'{num_a} + {num_b} = {num_c}')
            return
            
def main():
    calculate_permutations('send', 'more', 'money')

if __name__ == '__main__':
    main()
