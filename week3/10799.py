
answer = cnt = 0
for i in input():
    print(cnt)
    if i == '(':
        cnt += 1
    else:
        cnt -= 1
        answer += cnt
    
print(answer)