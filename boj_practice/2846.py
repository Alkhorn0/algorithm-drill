# 구현 문제
n = int(input())
heights = list(map(int, input().split()))
ascend = []
slope = 0
for i in range(n-1):
    if heights[i] < heights[i+1]:
        slope += heights[i+1] - heights[i]
    elif heights[i] >= heights[i+1]:
        ascend.append(slope)
        slope = 0
ascend.append(slope)
print(max(ascend))
