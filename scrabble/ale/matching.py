import itertools

board = [['',  '', '', ''],
         ['', 'c', '', ''],
         ['', 'a', '', ''],
         ['', 't', '', '']]
letters_values = {'a': 1, 'b': 3, 'c': 2, 'd': 3, 'e': 1, 'f': 4}
valid_words = ['cat', 'dog', 'bird', 'hippo', 'cab', 'face', 'feed']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'e']

# tries = []
# try_words = []
try_words = set()
i = 0
for length in range(len(letters)):
    for word_letters in itertools.combinations(letters, length + 1):
        # print(''.join(word))
        for word in itertools.permutations(word_letters):
            if ''.join(word) in valid_words:
                # try_words.append(word)
                try_words.add(word)
            i += 1
# print(tries)
print(try_words)
print(i)
