word = input("Pick a word, any word!! Anything that comes to mind!! ")

def letterCount(word):
    word = word.lower()
    dictionary = {"a": 0, "c": 0, "b": 0, "e": 0, "d": 0, "g": 0, 
    "f": 0, "i": 0, "h": 0, "k": 0, "j": 0, "m": 0, 
    "l": 0, "o": 0, "n": 0, "q": 0, "p": 0, "s": 0, 
    "r": 0, "u": 0, "t": 0, "w": 0, "v": 0, "y": 0, 
    "x": 0, "z": 0}
    for l in word:
        dictionary[l] += 1
    return dictionary

print(letterCount(word))
