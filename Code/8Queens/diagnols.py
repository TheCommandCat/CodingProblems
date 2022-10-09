def isDiagnolsValid(b, num, letter, returnList = False):
    diagnolslist= []
    for j in range(1,8):
        if (num+j != 8) and (letter+j !=8) and (num+j == abs(num+j)) and (letter+j == abs(letter+j)):
            diagnolslist.append([num+j, letter + j])
        else:
            break
    for j in range(1,8):
        if num+j != 8 and letter-j != 8 and num+j == abs(num+j) and letter-j == abs(letter-j):
            diagnolslist.append([num+j, letter - j])
        else:
            break
    for j in range(1,8):
        if num-j != 8 and letter-j != 8 and num-j == abs(num-j) and letter-j == abs(letter-j):
            diagnolslist.append([num-j, letter - j])
        else:
            break
    for j in range(1,8):
        if num-j != 8 and letter+j != 8 and num-j == abs(num-j) and letter+j == abs(letter+j):
            diagnolslist.append([num-j, letter + j])
        else:
            break
    if returnList:
        return diagnolslist

    valid = True

    for i in diagnolslist:
        if b[i[0], i[1]] == 1:
            valid = False
            break
    return valid