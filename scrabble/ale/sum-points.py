word = "jugend"
valueschar = {"j":1, "u":1, "g":2, "e":1, "n":1, "d":2}

word_score = 0

for l in word:
charvalue = valueschar[l]
word_score += charvalue

print(f'the total score for the word is: {word_score}')
