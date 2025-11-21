from random import choice
def ListOfWords():
    file = open("wordSearchGenerator/words.txt")
    listWords = []
    listWords = addToList(file, listWords)
    file.close()
    return listWords

def addToList(file, listWords):
    with file as f:
        for word in f:
           listWords.append(word.strip())
    return listWords


def charfiller(matrix, wordlist):
    chars = getChars(wordlist)
    lengthMatrix = len(matrix)

    totalMatrix = lengthMatrix * lengthMatrix
    quantityPerChar = totalMatrix // len(chars)

    while totalMatrix != 0:
        for i in range(lengthMatrix):
            for j in range(lengthMatrix):
                if matrix[i][j] == 0:
                    matrix[i][j] = choice(chars)
        totalMatrix -=1
    return matrix

def getChars(wordlist):
    allchars = []
    for word in wordlist:
        for char in word:
            if char not in allchars:
                allchars.append(char)
    return allchars
