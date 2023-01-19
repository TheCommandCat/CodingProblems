
#solve takes a set and return a set of sets(all the sub sets)

s = []

def solve(Set(s)):
    # s stands for set object

    if output == []:
        return output
    
    for i in s:
        

        a = solve(s-i)
        for j in a:
            b = b + (j+i) + j

        return(b)
