
# way 1:


def display(solution_number, board):
    row = '|   ' * len(board) + '|'
    hr  = '+---' * len(board) + '+'
    for column in board:
        print(hr)
        print(row[:column*4-3],'Q',row[column*4:])
    print(f'{hr}\n{board}\nSolution - {solution_number}\n')

def issafe(queen, board, x=1):
    if not board:
        return True
    if board[-1] in [queen+x,queen-x]: 
        return False
    return issafe(queen, board[:-1], x+1)

def solve(boardsize, board=[], solutions_found=0):
    if len(board) == boardsize:
        solutions_found += 1
        display(solutions_found, board)
    else:
        for queen in [column for column in range(1,boardsize+1) if column not in board]:
            if issafe(queen,board):
                solutions_found = solve(boardsize, board + [queen], solutions_found)
    return solutions_found

if __name__ == '__main__':
    solutions = solve(8)
    print(f'{solutions} solutions found')

# way 2:

def display(solution_number, board):
    row = '|   ' * len(board) + '|'
    hr  = '+---' * len(board) + '+'
    for column in board:
        print(hr)
        print(row[:column*4-3],'Q',row[column*4:])
    print(f'{hr}\n{board}\nSolution - {solution_number}\n')

def issafe(queen, board, x=1):
    if not board: 
        return True
    if board[-1] in [queen+x,queen-x]: 
        return False
    return issafe(queen, board[:-1], x+1)

def solve(boardsize, board=[]):
    if len(board) == boardsize:
        yield board
    else:
        for queen in [column for column in range(1,boardsize+1) if column not in board]:
            if issafe(queen,board):
                yield from solve(boardsize, board + [queen])

if __name__ == '__main__':
    for solutionnumber, solution in enumerate(solve(8)):
        display(solutionnumber+1, solution)

