import numpy as np
from diagnols import findDiagnols

b = np.zeros((8, 8), dtype=int)

# code to cords example: B4 = (2, 4)

def ctc(code):
    letter = [i for i in code][0]
    num = [i for i in code][1]
    listLettersToNumbers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    letter = listLettersToNumbers[letter]
    return 7 - (int(num) - 1), int(letter) - 1 

def placeq(code):
    num, letter = ctc(code)
    b[num, letter] = 1

def checkvalid(code, visualize=False):
    num, letter = ctc(code)
    print("cords:", letter, num)
    print(np.count_nonzero(b[num] == 1), np.count_nonzero(b[:, letter] == 1))
    valid = (np.count_nonzero(b[num] == 1) <= 1) and (np.count_nonzero(b[:, letter] == 1) <= 1)
    diaglist = findDiagnols(num, letter)
    for i in diaglist:
        if b[i[0], i[1]] == 1:
            valid = False
            break
    print("valid:", valid)
    if visualize:
        b[num] = 10
        b[:,letter] = 10
        for i in diaglist:
            b[i[0], i[1]] = 10
        placeq(code)

# all machanics are finished
# write here the algorithm ↓

