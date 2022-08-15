import numpy as np

b = np.zeros((8, 8), dtype=int)

# code to cords example: B4 = (2, 4)

def ctc(code):
    letter = [i for i in code][0]
    num = [i for i in code][1]
    listLettersToNumbers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    letter = listLettersToNumbers[letter]
    return int(letter) - 1, 7 - (int(num) - 1)

def placeq(code):
    letter, num = ctc(code)
    b[num, letter] = 1

def diagnols(code):
    letter, num = ctc(code)
    diagnolslist= []
    for i in range(1, 4):
        match i:
            case 1:
                for j in range(1,8):
                    if num+j != 9 and letter+j != 9 and num+j != -1 and letter+j != -1:
                        diagnolslist.append([num+j, letter + j])
                    else:
                        break
            case 2:
                for j in range(1,8):
                    if num+j != 9 and letter-j != 9 and num+j != -1 and letter-j != -1:
                        diagnolslist.append([num+j, letter - j])
                    else:
                        break
            case 3:
                for j in range(1,8):
                    if num-j != 9 and letter-j != 9 and num-j != -1 and letter-j != -1:
                        diagnolslist.append([num-j, letter - j])
                    else:
                        break
            case 4:
                for j in range(1,8):
                    if num-j != 9 and letter+j != 9 and num-j != -1 and letter+j != -1:
                        diagnolslist.append([num-j, letter + j])
                    else:
                        break
    return (diagnolslist)


def checkvalid(code, visualize=False):
    letter, num = ctc(code)
    print("cords:", letter, num)
    valid = (np.count_nonzero(b[letter] == 1) <= 1) and (np.count_nonzero(b[:, letter] == 1) <= 1)
    diagnoals = []

    diagnoals.append((num+1, letter+1))
    print("valid:", valid)
    if visualize:
        b[num] = 2
        b[:,letter] = 2
        placeq(code)

placeq("B3")
dlist = diagnols("B3")
checkvalid("B3", visualize=True)
print(b)
