import sys
input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x : int) -> None:
        self.stack.append(x)
    
    def pop(self) -> int:
        try:
            return self.stack.pop()
        except IndexError:
            return -1
    
    def size(self) -> int:
        return len(self.stack)

    def empty(self) -> int:
        if len(self.stack) == 0:
            return 1
        return 0
    
    def top(self) -> int:
        try:
            return self.stack[-1]
        except IndexError:
            return -1

stack = Stack()
for i in range(int(input())):
    command = input().strip().split(" ")
    
    c = command[0]
    if c == 'push':
        stack.push(int(command[1]))
    elif c == 'top':
        print(stack.top()) 
    elif c == 'size':
        print(stack.size())
    elif c == 'empty':
        print(stack.empty())
    elif c == 'pop':
        print(stack.pop())