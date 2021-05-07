# 다이나믹 프로그래밍
n = int(input())
d = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    paint = list(map(int, input().split()))
    for j in range(3):
        if j == 0:
            d[i][j] = min(d[i-1][1],d[i-1][2])+paint[j]
        elif j == 1:
            d[i][j] = min(d[i-1][0],d[i-1][2])+paint[j]
        else:
            d[i][j] = min(d[i-1][0],d[i-1][1])+paint[j]
print(min(d[n]))