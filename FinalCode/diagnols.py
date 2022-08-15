def findDiagnols(num, letter):
    print("cords:", num, letter)
    diagnolslist= []
    for i in range(1, 5):
        match i:
            case 1:
                for j in range(1,8):
                    if num+j != 8 and letter+j != 8 and num+j == abs(num+j) and letter+j == abs(letter+j):
                        diagnolslist.append([num+j, letter + j])
                    else:
                        break
            case 2:
                for j in range(1,8):
                    if num+j != 8 and letter-j != 8 and num+j == abs(num+j) and letter-j == abs(letter-j):
                        diagnolslist.append([num+j, letter - j])
                    else:
                        break
            case 3:
                for j in range(1,8):
                    if num-j != 8 and letter-j != 8 and num-j == abs(num-j) and letter-j == abs(letter-j):
                        diagnolslist.append([num-j, letter - j])
                    else:
                        break
            case 4:
                for j in range(1,8):
                    if num-j != 8 and letter+j != 8 and num-j == abs(num-j) and letter+j == abs(letter+j):
                        diagnolslist.append([num-j, letter + j])
                    else:
                        break
    return diagnolslist