import collections

n, k = input().split(" ")
q = collections.deque(range(1, n))

cnt = 1
while q:
    if cnt % 3 == 0:
        q.pop()
