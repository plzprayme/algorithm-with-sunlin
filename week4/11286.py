from queue import PriorityQueue
import sys
input = lambda: int(sys.stdin.readline().strip())

nums = PriorityQueue()
for i in range(input()):
    n = input()
    if n == 0:
        nums.put(abs(n), n)
        continue
    
    try:
        print(nums.get()[1])
    except:
        print(0)