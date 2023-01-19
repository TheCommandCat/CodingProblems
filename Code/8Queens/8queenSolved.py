def checkBoard(position, nextRow):
    qList = position
    positionsCopy = qList.copy()
    positionsCopy.append(nextRow)
    if len(positionsCopy) != len(set(positionsCopy)):
        return False
    # untile here it should work
    for i in range(len(positionsCopy)):
        
        for j in range(len(positionsCopy)):
            
            if i != j:
                if i - j == positionsCopy[i]-positionsCopy[j] or j-i == positionsCopy[i]-positionsCopy[j]:
                    return False


    # for i in range(len(qList)):
    #     if col - qList[i] != i+1 - len(positionsCopy) and qList[i] - col != i+1 - len(positionsCopy):
    #         return False
    return True

def solve(positions):
    #return all solutions that start with the given k-1 positions, 
    if len(positions) == 8:
        output = (positions,)
        #print("return with solution",positions,output)
        return output

    output=()
    for i in range(1, 9):
        nextPositions=positions.copy()
        if checkBoard(positions, i):
            nextPositions.append(i)
            nextResults=solve(nextPositions)
            output += (nextResults)
        
    #print("return with output",positions,output)
    return output
        

print(checkBoard([3,6,2,7,1,5],8))

a=solve([3,6,2,7])
print(len(a))
for x in a:
    print(x)
    
a=solve([])
print(len(a))
for x in a:
    print(x)