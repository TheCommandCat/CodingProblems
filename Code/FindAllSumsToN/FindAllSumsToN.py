
# solve func takes a num and return a list of all ways to represent the num as a sum of natural nums

def solve(n):
    print("n: ",type(n), n)
    
    if n == 1:
        return [1]

    # 5
    # 1 2 3 4
    
    y = []
    for i in range(n-1):
        x = solve(n-(i+1))
        print("x", x)
        # for j in x:
        #     print("x: ", x, "j: ", j, "i: ", i)
        #     y = [y for y in ]
        y = [[z, 1] for z in x]
        print(y)

    return y


print(solve(5))
