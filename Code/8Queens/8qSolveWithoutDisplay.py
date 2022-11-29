# // 8 queen problem without display esay?

def solve(n):
    if n == 0: return [[]] # No RECURSION if n=0. 
    smaller_solutions = solve(n-1) # RECURSION!!!!!!!!!!!!!!
    solutions = []
    for solution in smaller_solutions:# I moved this around, so it makes more sense
        for column in range(1,8+1): # I changed this, so it makes more sense
            # try adding a new queen to row = n, column = column 
            if not under_attack(column , solution): 
                solutions.append(solution + [(n,column)])
    return solutions


def under_attack(column, existing_queens):
    # ASSUMES that row = len(existing_queens) + 1
    row = len(existing_queens)+1
    for queen in existing_queens:
        r,c = queen
        if r == row: return True # Check row
        if c == column: return True # Check column
        if (column-c) == (row-r): return True # Check left diagonal
        if (column-c) == -(row-r): return True # Check right diagonal
    return False


print(solve(8))