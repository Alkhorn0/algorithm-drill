# 다이나믹 프로그래밍
n = int(input())
a = [0] + [list(map(int, input().split())) for _ in range(n)]
d = [[0 for j in range(i)] for i in range(n+1)]
d[1][0] = a[1][0]
for i in range(2, n+1):
    for j in range(i):
        if j == 0:
            d[i][0] = d[i-1][0]+a[i][0]
        elif j == i-1:
            d[i][i-1] = d[i-1][-1]+a[i][-1]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j])+a[i][j] 
print(max(d[n]))