from random import choice, randint

def generateMatrix(cantidad):
    Matrix= [] 
    row=[] 
    for i in range(cantidad): 
        row=[] 
        for j in range(cantidad): 
            row.append(0)
        Matrix.append(row)
    return Matrix

def printMatrix(Matrix):
    for row in Matrix:
        print(row) 



def putWordinMatrix(matrix, wordList, direction):
    lengthMatrix = len(matrix)

    for word in wordList:
        selectedDirection = choice(direction)
        lengthWord = len(word)

        if selectedDirection == 1:  # A-B
            pass
        if selectedDirection == 2:  # B-A
            pass
        if selectedDirection == 3:  # D-I
            pass
        if selectedDirection == 4:  # I-D
            pass
    return matrix

def spaceVerification(matrix, i, j):
    if matrix[i][j] == 0:
        return True
    else:
        return False
    
def wordSpaceVerification(matrix, i, j, direction, lengthWord):
    if direction == 1:  # A-B
        for k in range(lengthWord):
            if not spaceVerification(matrix, i+k, j):
                return False

    if direction == 2:  # B-A
        for k in range(lengthWord):
            if not spaceVerification(matrix, i-k, j):
                return False

    if direction == 3:  # D-I
        for k in range(lengthWord):
            if not spaceVerification(matrix, j, i+k):
                return False

    if direction == 4:  # I-D
        for k in range(lengthWord):
            if not spaceVerification(matrix, j, i-k):
                return False

    return True

def verifyStartPosition(lengthWord, lengthMatrix, direction):
    if direction == 1:
        i = randint(0, lengthMatrix - lengthWord)
        j = randint(0, lengthMatrix - 1)
        return i, j
    if direction == 2:
        pass
    if direction == 3:
        pass
    if direction == 4:
        pass


def directionUpDown(matrix, word, lengthWord, lengthMatrix):
    ir, jr = verifyStartPosition(lengthWord, lengthMatrix, 1)
    for i in range(lengthWord):
        matrix[ir+i][jr] = word[i]
    return matrix

def directionDownUp(matrix, word, lengthWord, lengthMatrix):
    ir, jr = verifyStartPosition(lengthWord, lengthMatrix, 2)
    for i in range(lengthWord):
        matrix[ir-i][jr] = word[(lengthWord-1)-i]
    return matrix

def directionRightLeft(matrix, word, lengthWord, lengthMatrix):
    ir, jr = verifyStartPosition(lengthWord, lengthMatrix, 3)
    for i in range(lengthWord):
        matrix[jr][ir+i] = word[i]
    return matrix

def directionLeftRight(matrix, word, lengthWord, lengthMatrix):
    ir, jr = verifyStartPosition(lengthWord, lengthMatrix, 4)
    for i in range(lengthWord):
        matrix[jr][ir-i] = word[i]
    return matrix
