def validID(ID):
    import math
    id = str(ID)
    sepratedID = [*id]
    for i in range(len(sepratedID)):
        sepratedID[i] = str(int(sepratedID[i]) * int(1 if (i % 2 == 0) else 2))
    for i in range(len(sepratedID)):
        if len(sepratedID[i]) > 1:
            sepratedID[i] = str(sum(map(int, sepratedID[i])))
    sumOfAllNums = sum(map(int, sepratedID))
    roundedUpNum = math.ceil(sumOfAllNums / 10) * 10
    print(roundedUpNum - sumOfAllNums)