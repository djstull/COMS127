def vowelfinder(word):
    for i in range (len(word)):
        if word[i] in ["a", "e", "i", "o", "u"]:
            return i
    return -1

print(vowelfinder("arin the angry aardvark"))