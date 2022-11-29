# // how to solve 8 queen problem?


def display(solution_number, board):
    row = '|   ' * len(board) + '|'
    hr  = '+---' * len(board) + '+'
    for col in board:
        print(hr)
        print(row[:col*4-3],'Q',row[col*4:])
    print(f'{hr}\n{board}\nSolution - {solution_number}\n')

def issafe(q, board, x=1):
    if not board: return True
    if board[-1] in [q+x,q-x]: return False
    return issafe(q, board[:-1], x+1)

def solve(boardsize, board=[], solutions_found=0):
    if len(board) == boardsize:
        solutions_found += 1
        display(solutions_found, board)
    else:
        for q in [col for col in range(1,boardsize+1) if col not in board]:
            if issafe(q,board):
                solutions_found = solve(boardsize, board + [q], solutions_found)
    return solutions_found

if __name__ == '__main__':
    solutions = solve(8)
    print(f'{solutions} solutions found')


def display(solution_number, board):
    row = '|   ' * len(board) + '|'
    hr  = '+---' * len(board) + '+'
    for col in board:
        print(hr)
        print(row[:col*4-3],'Q',row[col*4:])
    print(f'{hr}\n{board}\nSolution - {solution_number}\n')

def issafe(q, board, x=1):
    if not board: return True
    if board[-1] in [q+x,q-x]: return False
    return issafe(q, board[:-1], x+1)

def solve(boardsize, board=[]):
    if len(board) == boardsize:
        yield board
    else:
        for q in [col for col in range(1,boardsize+1) if col not in board]:
            if issafe(q,board):
                yield from solve(boardsize, board + [q])

if __name__ == '__main__':
    for solutionnumber, solution in enumerate(solve(8)):
        display(solutionnumber+1, solution)


def issafe(q, board):
    x = len(board)
    for col in board:
        if col in [q+x,q-x]: return False
        x -= 1
    return True


