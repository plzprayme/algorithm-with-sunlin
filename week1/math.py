
# a, b, c, d, e, f = 1,3,-1,4,1,7 # 2 -1
a, b, c, d, e, f = 2,5,8,3,-4,-11 # -1 2

# a, b, c, d, e, f = map(int, input().split(" "))



flag = 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            flag = 1
            break
    if flag == 1:
        break