

num = int(input())
answer = 0

for i in range(num):
    constructor = i + sum(map(int, str(i)))
    if num == constructor:
        answer = i
        print(answer)
        break
if answer == 0:    
    print(answer)