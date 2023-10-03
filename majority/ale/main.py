items = [1, 1, 2, 1, 3, 1]

occurrences = {}
for item in items:
    # print(item)
    if item in occurrences:
        occurrences[item] += 1
    else:
        occurrences[item] = 1
# print(occurrences)
majority_item = None
majority_count = 0
for key, value in occurrences.items():
    # print(key, value)
    if value > majority_count:
        majority_count = value
        majority_item = key
print(f'{majority_item}: {majority_count}')

# O(2n)
# O(n)
