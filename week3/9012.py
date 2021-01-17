

def solution(ps):
    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                return "NO"
    if stack:
        return "NO"
    return "YES"

for i in range(int(input())):
    print(solution(input()))

