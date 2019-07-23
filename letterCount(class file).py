word = input('Pick a word, a string, or phrase. Anything, just do it with haste. ')

def letterCount(word):
    word = word.lower()
    letterCountDict = {}
    for l in word:
        if(l in letterCountDict):
            letterCountDict[l] += 1
        else:
            letterCountDict[l] = 1
    return letterCountDict

print(letterCount(word))
