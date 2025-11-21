#importing modules
import wordList as wl
import basicFunctions as bf

#logic
def main():
    matrix = 10
    wsDifficulty = 3

    beggingWordSearchGenerator(matrix, wsDifficulty)

def beggingWordSearchGenerator(matrixSize, difficulty):
    ws = bf.generateMatrix(matrixSize)
    wsDifficulty = selectDificulty(difficulty)
    wordlist = wl.ListOfWords()

    bf.putWordinMatrix(ws, wordlist, wsDifficulty)
    wl.charfiller(ws, wordlist)
    print(bf.printMatrix(ws))
    return ws

def selectDificulty(int):
 # Up to Down
    if int == 1:
        return [1]
    
 # Up to Down
 # Down to Up
    if int == 2:
        return [1,2]
    
 # Up to Down
 # Down to Up
 # Left to Right
 # Right to Left
    if int == 3:
        return [1,2,3,4]
    
 # up to down
 # down to up
 # left to right
 # right to left
 # diagonals *TODO*
    if int == 4: 
        return [1,2,3,4,5,6,7,8] 
    

#main program execution
main()