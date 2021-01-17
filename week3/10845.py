import sys
import collections
input = sys.stdin.readline 

q = collections.deque()
for i in range(int(input())):
    c = input().strip().split(" ")
    
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        try: 
            print(q.popleft())
        except:
            print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif c[0] == 'back':
        try:
            print(q[-1])
        except:
            print(-1)
