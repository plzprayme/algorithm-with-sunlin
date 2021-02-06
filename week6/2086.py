# 나무 M미터가 필요하다.

# 높이 H를 정한다. <- 톱날이 시작하는 위치
# 높이가 H보다 작으면 잘리지 않는다.
# H보다 크면 H 위의 부분부터 잘린다.

import sys
input = lambda:map(int, sys.stdin.readline().strip().split())

N, M = input()
woods = sorted(input())

left_height, right_height = 1, 2_000_000_000
answer = 0
while left_height <= right_height:
    H = (right_height + left_height) // 2

    cutted = sum(map(lambda x: x-H, [a for a in woods if a>H]))
    if cutted == M:
        answer = H
        break
    elif cutted > M:
        answer = H
        left_height = H
    elif cutted < M:
        right_height = H
print(answer)