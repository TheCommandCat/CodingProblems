
# solve func takes a num and return a list of all ways to represent the num as a sum of natural nums
def solve(n):
    
    # 5
    # 1 2 3 4
    

    for i in range(n-1):
        x = solve(n-i)
        for j in x:
            y = [i].append(x)


    return y
print([2,3].extand([4,3]))
print((1,2) + (3,4,5))