soldiers_n = 41
step = 3

soldiers = list(range(1, soldiers_n + 1))
# soldiers = list(range(soldiers_n))

# # print(soldiers)
# for i, soldier in enumerate(soldiers):
#     if i % step == 0:
#         #print(i, soldier)
#         # soldiers.remove(i)
#         del soldiers[i]
# print(soldiers)

# while len(soldiers) > 1:
#     for i, soldier in enumerate(soldiers):
#         if i % step == 0:
#             print(soldier)
#             del soldiers[i]
# print(soldiers)

i = 0
alive = []
while len(soldiers) > 1:
    if (i % step) != 0:
        print('+ ' + str(soldiers[i]))
        alive.append(soldiers[i])
    i += 1
    if i >= len(soldiers):
        i = (i - 1) % step
        soldiers = alive
print(soldiers)

