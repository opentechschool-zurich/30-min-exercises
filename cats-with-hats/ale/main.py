cats = [False] * 100

for i in range(1, 101):
    for j in range(0, 100, i):
        cats[j] = not cats[j]

for i, cat in enumerate(cats):
    if cat:
        print(i)
