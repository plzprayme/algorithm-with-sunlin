nums = []
for i in range(int(input())):
    nums.append(int(input()))

answer = []
while nums:
    left, right = 0, 1
    mn = nums[left]
   
    while right < len(nums):
        mn = min(mn, nums[right])
        right += 1
    nums.remove(mn)
    answer.append(mn)
    left += 1

for i in answer:
    print(i)
# print(answer)