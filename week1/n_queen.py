import collections

n = int(input())

# 대각 위왼 = -n-1
# 위 = -n
# 대각 위오 = -n+1
# 왼,오 = -1,+1
# 대각 아왼 = +n-1
# 대각 아 = +n
# 대각 아오 = +n+1


flag = 0
def attack_range(direction):
    for i in range(position+direction, 0, direction):
        board[i] += 1
        if board[i] > 1:
            flag = 1
            break
        print(f'i: {i}, position: {position}')


size = n*n
position = collections.Counter(range(25))

board = collections.defaultdict(int)
for queen in range(n):
    # 왼위
    for position in range(n*n):
        if flag == 0:
            attack_range(-n-1)
        if flag == 0:
            attack_range(-n)
        if flag == 0:
            attack_range(-n+1)
        if flag == 0:
            attack_range(-1)
        

        # for i in range(position-n-1, 0, -n-1):
        #     board[i] += 1
        #     if board[i] > 1:
        #         break
            # print(f'Queen: {queen}, position: {position} i: {i}')

        for i in range(position-n, 0, -n):
            board[i] += 1
            if board[i] > 1:
                break
        
        # 대각 위왼 = -n-1
        # 위 = -n
        # 대각 위오 = -n+1
        # 왼,오 = -1,+1
        # 대각 아왼 = +n-1
        # 대각 아 = +n
        # 대각 아오 = +n+1
