# 구현문제 
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for __ in range(n)]

min_time, height = 100000000000000000000000000, 0

for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if ground[j][k] < i:
                min += (i - ground[j][k])  # 메꿀 블럭 수
            else:
                max += (ground[j][k] - i)  # 파낼 블럭 수
    inventory = max + b                     # 인벤토리에 들어있을 블럭 수
    if inventory < min:       # 메꿔야 할 블럭이 인벤토리에 있는 것 보다 많으면 못 메꾸므로 패스
        continue
    time = 2*max + min
    if time <= min_time:
        min_time = time
        height = i

print(min_time, height)
