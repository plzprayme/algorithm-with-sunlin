import itertools
import sys

a = int(input())
nums = list(map(int, input().split(" ")))
p = map(int , input().split(" "))

op = []
for o, n in zip([0, 1, 2, 3], p):
    for i in range(n):
        op.append(o)

sheet = {
    0: lambda a,b: a+b,
    1: lambda a,b: a-b,
    2: lambda a,b: a*b,
    3: lambda a,b: -(abs(a)//b) if a<0 else a//b
}

m, n = -sys.maxsize, sys.maxsize

expression = set(itertools.permutations(op))
for e in expression:
    result = nums[0]
    for i in range(len(nums)-1):
        result = sheet[e[i]](result, nums[i+1])
    m = max(m, result)
    n = min(n, result)


print(m, n)

