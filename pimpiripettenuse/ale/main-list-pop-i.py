soldiers_n = 41
step = 3

soldiers = list(range(1, soldiers_n + 1))

i = 0
while len(soldiers) > 1:
    while i < len(soldiers):
        soldier = soldiers.pop(i)
        print('+ i', i, soldier)
        i += step - 1
    # print('>>> len', len(soldiers), 'i ', i, i - len(soldiers))
    i -= len(soldiers)
print(soldiers, i)
