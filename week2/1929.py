m,n = 1, 10000000

# m,n = map(int, input().split(" "))

a = [i for i in range(n+1)]
b = 2
while b < n//2:
    i = 2
    while b*i <= n:
        a[b*i] = -1
        i += 1
    b += 1

for i in a[m:n+1]:
    if i != -1:
        print(i)