def is_safe(board,row,col,N):
    for i in range(col):
        if board[row][i] ==1 :
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False

    return True

def solve_n_queens_util(board,col,N):
    if col>=N:
        return True

    for i in range(N):
        if is_safe(board,i,col,N):
            board[i][col]=1
            if solve_n_queens_util(board,col+1,N):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(N):
    board = [[0 for _ in range(N)]for _ in range(N)]
    if not solve_n_queens_util(board,0,N):
        print('False')
        return False
    print_solution(board)
    return True

def print_solution(board):
    for col in board:
        for row in col:
            print(row,end=" ")
        print()

solve_n_queens(10)