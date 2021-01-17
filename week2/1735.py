a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))

# 통분

son = a*d + b*c 
mom = b*d

mod = -1
mx, mn = max(son, mom), min(son,mom)
while mod != 0:
    mod = mx % mn
    mx, mn = mn, mod

print((a*d + b*c) // mx, b*d // mx)