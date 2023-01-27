
# solve func takes a num and return a lst of all ways to represent the num as a sum of natural nums

def solve(n):
    if n == 1:
        return[[1]]
    lst = [[n]]
    for i in range(1, n):
        for j in solve(n-i):
            lst += [j + [i]]
    return lst


print(solve(3))
