
from operator import le
import numpy as np
from diagnols import isDiagnolsValid



# all "chess code" old code

def ctc(code):
    letter = [i for i in code][0]
    num = [i for i in code][1]
    listLettersToNumbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    letter = int(listLettersToNumbers[letter])
    # origanli it is return 7 - (int(num) - 1)
    return 8 - num, letter

# nicer way to write b[num, letter] = 1

def placeq(num, letter, numToplace):
    b[num, letter] = numToplace

def checkvalid(num, letter, b, visualize=False):
    placeq(num, letter , 1)
    validRowsAndColumns = (np.count_nonzero(b[num] == 1) <= 1) and (np.count_nonzero(b[:, letter] == 1) <= 1)
    validDiagnols = isDiagnolsValid(b, num, letter)
    valid = validRowsAndColumns and validDiagnols
    if valid:
        print("valid:", valid)
    if visualize and valid: # works only at first time, debug use only

        for i in range(8):
            print(num, letter, i)
            if b[num, i] != 1:
                placeq(num, i, 2)
        for i in range(8):
                if b[i, letter] != 1:
                    placeq(i, letter, 2)

        diaglist = isDiagnolsValid(b, num, letter, returnList=True)
        for i in diaglist:
            if b[i[0], i[1]] != 1:
                b[i[0], i[1]] = 2
    if not valid:
        b[num, letter] = 0
    return valid

numOfQueens = 0

# all machanics are finished
# write here the algorithm ↓


b = np.zeros((8, 8), dtype=int)
for i in range(8):
    for j in range(8):
        if checkvalid(i, j, b, visualize = True):
            placeq(i,j, 1)
    




print(b)