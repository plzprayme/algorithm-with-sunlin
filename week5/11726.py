# 2xn
# 1x2, 2x1
import sys
import collections
input = lambda : int(sys.stdin.readline().strip())

n = input()

if n <= 3:
    print(n)

else:
    memory = collections.defaultdict()
    for i in range(4):
         memory[i] = i


    for i in range(4, n+1):
        memory[i] = memory[i-1] + memory[i-2]
        
    print(memory[n] % 10007)



    
