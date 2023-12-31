# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
# O(n) + space O(1) if it's known that there an absolute majority


items = [1, 1, 2, 1, 3, 1]

majority_item = None
i = 0;
for item in items:
    if i == 0:
        majority_item = item
        i = 1
    elif majority_item == item:
        i += 1
    else:
        i -= 1
print(majority_item)
