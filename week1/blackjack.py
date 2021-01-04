cards, black_jack= map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

answer = -1
for i in range(cards-2):
    for j in range(i+1, cards):
        for k in range(j+1, cards):
            num = nums[i]+nums[j]+nums[k]

            if num == black_jack:
                answer = num
                break

            if num < black_jack:
                answer = max(answer, num)


        if answer == black_jack:
            break

    if answer == black_jack:
        break
            
print(answer)


