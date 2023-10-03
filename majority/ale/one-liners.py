from collections import Counter
items = [1,2,3,4,3,3,2,4,5,6,1,2,3,4,5,1,2,3,4,6,5];
print(Counter(items).most_common()[0])


# https://stackoverflow.com/a/48106950/5239250
l = [1,2,3,4,3,3,2,4,5,6,1,2,3,4,5,1,2,3,4,6,5]
print(max(set(l), key = l.count))
