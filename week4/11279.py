import heapq
import sys
input = lambda : int(sys.stdin.readline().strip())

nums = []
for i in range(input()):
    n = input()
    if n > 0:
        heapq.heappush(nums,-n)
        continue

    try:
        print(-heapq.heappop(nums))
    except:
        print(0)