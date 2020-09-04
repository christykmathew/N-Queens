from func import N_Queen as nq
def n_queen(board,row,n):
    flag = 1
    # if (row >= n or row < 0):
    #   return
    if (row < n and 'Q' in board[row]):
        index = board[row].index('Q')
        board[row][index] = '-'
        for i in range(index+1, n):
            flag = queens.check(board,row,i)
            if (flag == 0):
                board[row][i] = 'Q'
                n_queen(board, row+1, n)
                return
        if (flag == 1 and row-1 >= 0):
            n_queen(board, row-1, n) 
            return
    for i in range(0,n):
        flag = queens.check(board,row,i)
        if (flag == 0):
            board[row][i] = 'Q'
            if(row == n-1):
               queens.board_draw(board)
                # print("\n")
                # if(board[0].index('Q') < n-1 and row-1 >= 0):
                #   n_queen(board, row-1,n) 
               return
            n_queen(board, row+1, n)
            break 
    if (flag == 1 and row-1 >= 0):
        n_queen(board, row-1, n)


board_input = []
queens = nq()
board_input =queens.initialise()
head = str(queens.n) + '-Queen Solution is/are:\n'
print(head)
n_queen(board_input, 0, queens.n)