
#solve takes a set and return a set of sets(all the sub sets) with recursion


s = [1,2,3,4,5,6,7]

def solve(s):
    # s stands for set object
    if s == [] or None:
        return [[]]
    
    subArrs = solve(s[:-1])   
    # print("subArrs: ", subArrs)
    lastObject = [s[-1]]
    # print("lastObject: ", lastObject)
    output = subArrs + [lastObject + i for i in subArrs]

    return output


# print(s[:-1]) # delete last object
# print(s[1:]) # delete first object
# print(s[-1]) # only last object as int


print(solve([1,5,9]))