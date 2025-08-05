soldiers_n = 41
step = 3

soldiers = list(range(1, soldiers_n + 1))

i = 0
while len(soldiers) > 1:
    soldier = soldiers.pop(0)
    if i % step == 0:
        print('+', i, soldier)
    else:
        soldiers.append(soldier)
    i += 1
print(soldiers, i)

