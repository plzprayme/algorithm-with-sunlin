import sys
input = lambda : int(sys.stdin.readline().strip())


num = input()

stairs = []
for i in range(num):
    stairs.append(input())

position = step = 0
while position < num:
    if step < 2:
        step += 1
        if position < num:
            print(stairs[position+1], stairs[position+2])
            position += 1

            continue
    
    step = 0
    position += 2


