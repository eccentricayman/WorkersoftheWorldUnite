import string

manifesto = open("manifesto.txt", "r")
manifestoList = manifesto.read().translate(None, string.punctuation).split()

def counter(count, toCount):
    return count + 1

def frequency(word):
    def hasWord(currentWord):
        return True if currentWord.lower() == word else False
    filterList = filter(hasWord, manifestoList)
    return len(filterList)

def totalFrequency(words):
    def hasWords(currentWord):
        return True if currentWord.lower() in words else False
    filterList = filter(hasWords, manifestoList)
    return len(filterList)

def mostFrequency():
    dictionary = {}
    def wordFreq(currentWord):
        if (currentWord in dictionary.keys()):
            dictionary[currentWord] += 1
        else:
            dictionary[currentWord] = 1
    map(wordFreq, manifestoList)
    mostFrequentWord = ""
    mostFrequentWordCount = 0
    for word, count in dictionary.items():
        if count > mostFrequentWordCount:
            mostFrequentWord = word
            mostFrequentWordCount = count
    return mostFrequentWord + ": " + str(mostFrequentWordCount) + " appearances"

print frequency("bourgeoisie")
print frequency("proletariat")

print totalFrequency(['bourgeoisie', 'proletariat'])

print mostFrequency()
