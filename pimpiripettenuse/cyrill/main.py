# people = 13
people = 31
n = 3

circle = list(range(1, people + 1))

i = 0
skip = n - 1
while sum(circle) > 0:
    if circle[i]:
        if skip > 0:
                skip -= 1
        else:
            print(circle[i], end = ' ')
            circle[i] = 0
            skip = n - 1
    i = (i + 1) % people
print()
