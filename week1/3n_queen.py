n = 8

# board = []
# for i in range(n):
#     board.append([0 for _ in range(n)])
# print(board)


position = []
for i in range(n):
    for j in range(n):
        flag = 0
        
        for r, c in position:
            if r == i:
                flag = 1
                break
            
            if c == j:
                flag = 2
                break
        
        if flag == 1:
            break

        if flag == 2:
            continue

        position.append((i,j))

print(position)