
# n = 110 # 99
# n = 1 # 1
# n = 210 # 105
# n = 1000 # 144

n = int(input())
answer = 0

if n < 100:
    print(n)
else:
    answer += 99
    for i in range(100, n+1):
        nums = list(map(int, str(i)))

        weight = nums[0] - nums[1]
        # if len(nums) > 2:
            # print(nums)
        i, flag = 1, 1
        while i < len(nums)-1:
            if nums[i]-nums[i+1] != weight:
                flag = 0
            i +=1

        if flag == 1:      
            answer += 1
    print(answer)