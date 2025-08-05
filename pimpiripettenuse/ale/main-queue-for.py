soldiers_n = 41
step = 3

soldiers = list(range(1, soldiers_n + 1))

while len(soldiers) > 1:
    soldier = soldiers.pop(0)
    print('+', soldier)
    for i in range(step - 1):
        soldiers.append(soldiers.pop(0))
print(soldiers, i)

