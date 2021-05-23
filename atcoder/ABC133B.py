import math
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (abs(x[i][k]-x[j][k]))**2
        dist = math.sqrt(dist)
        if dist == math.ceil(dist):
            ans += 1
print(ans)