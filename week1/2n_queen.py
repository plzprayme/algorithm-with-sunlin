
n = 8  # 92

board = []
for i in range(n):
    board.append([0 for i in range(n)])


def check_attack_range(board):
    board[row][column] = 1

    # 왼위
    i, j = row-1, column-n
    while i > 0 and j > 0:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        i, j = i-1, j-n

    # 위
    i, j = row-1, column
    while i > 0:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        i = i-1

    # 오위
    i, j = row-1, column+1
    while i > 0 and j < n:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        i, j = i-1, j+1

    # 왼
    i, j = row, column-1
    while j > 0:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        j = j-1

    # 오
    i, j = row, column+1
    while j < n:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        j = j+1

    # 왼아
    i, j = row+1, column-1
    while i < n and j > 0:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        i, j = i+1, j-1

    # 아
    i, j = row+1, column
    while i < n:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        i = i+1

    # 오아
    i, j = row+1, column+1
    while i < n and j < n:
        if board[i][j] == 1:
            flag = 1
            return
        board[i][j] = 1
        i, j = i+1, j+1
    
    return board
    



for row in range(n):
    for column in range(n):
        board = check_attack_range(board)
        
        for i in range(n):
            for j in range(n) :
                tmp_board = board[::]
                if tmp_board[i][j] == 1:
                    continue


                for k in range(j):
                    tmp_board2 = tmp_board[::]
                    if tmp_board[i][j] == 1:
                        continue
                    flag = 0
                    check_attack_range(tmp_board2)
                    if flag == 0:
                        tmp_board = tmp_board2[::]
                
                    
                    
                    
# print(f'{board}')



            


# print(board)
