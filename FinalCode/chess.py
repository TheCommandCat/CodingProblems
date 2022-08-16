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

def placeq(num, letter):
    # num, letter = ctc(code)
    b[num, letter] = 1

def checkvalid(num, letter, visualize=False):
    b[num, letter] = 1
    # num, letter = ctc(code)
    print("cords:", letter, num)
    valid = (np.count_nonzero(b[num] == 1) <= 1) and (np.count_nonzero(b[:, letter] == 1) <= 1)
    diaglist = findDiagnols(num, letter)
    for i in diaglist:
        if b[i[0], i[1]] == 1:
            valid = False
            break
    print("valid:", valid)
    if visualize:
        b[num] = 2
        b[:,letter] = 2
        for i in diaglist:
            b[i[0], i[1]] = 2
        placeq(num, letter)
    if not valid:
        b[num, letter] = 0
    return valid
numOfQueens = 0

# all machanics are finished
# write here the algorithm ↓

for x in range(8):
    for y in range(8):
        if checkvalid(x, y):
            placeq(x, y)
            numOfQueens += 1
print(b)
print("numOfQueens:", numOfQueens)