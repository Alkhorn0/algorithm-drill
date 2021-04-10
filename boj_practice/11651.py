# 정렬 문제
n = int(input())
points = []
for __ in range(n):
    points.append(list(map(int, input().split())))

points = sorted(points, key=lambda x : x[0])
points = sorted(points, key=lambda x : x[1])

for i in range(n):
    print(points[i][0], points[i][1])