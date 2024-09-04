"""generate prime numbers between two numbers"""

from math import sqrt

a = -10
b = 13

for i in range(max(a, 2), b + 1):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
