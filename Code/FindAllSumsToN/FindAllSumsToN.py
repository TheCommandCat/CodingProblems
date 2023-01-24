
# solve func takes a num and return a list of all ways to represent the num as a sum of natural nums
def solve(n):
    
    # s stands for set object
    if len(n) <= 0:
        return []
    if len(n) == 1:
        return [[1]]

    subArrs = solve(n-1)   
    # print("subArrs: ", subArrs)
    lastObject = n[:-1]
    # print("lastObject: ", lastObject)
    output = subArrs + [lastObject + i for i in subArrs]
    return output

print(solve([5]))