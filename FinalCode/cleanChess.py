import numpy as np
from diagnols import isDiagnolsValid

b = np.zeros((8, 8), dtype=int)
global numOfQueens
numOfQueens = 0


def placeq(num, letter, numToplace):
    b[num, letter] = numToplace



# checkvalid draw 
def placeIfValid(num, letter, b, visualize=False):
    global numOfQueens
    bn = b
    lastvalue = b[num, letter]
    bn[num, letter] = 5 # test
    valid = True
    for i in range(8):
        if bn[i, letter] != 1:
            placeq(i, letter, 2)
        else:
            valid = False
    for i in range(8):
        if bn[num, i] != 1:
            placeq(num, i, 2)
        else:
            valid = False
    dlist = isDiagnolsValid(bn, num, letter, returnList=True)
    for i in dlist:
        if bn[i[0], i[1]] != 1:
            placeq(i[0], i[1], 2)
        else:
            valid = False
    bn[num, letter] = lastvalue
    if valid:
        placeq(num, letter, 1)
        b = bn
        numOfQueens += 1




placeIfValid(0,0,b)
placeIfValid(1,1,b)
placeIfValid(4,1,b)
print(b, numOfQueens)
