# 다이나믹 프로그래밍
n = int(input())
d = [[0, 0, 0] for _ in range(100001)]
d[1] = [1, 1, 1]
mod = 9901
for i in range(2, n+1):
    d[i][0] = sum(d[i-1])%mod
    d[i][1] = (d[i-1][0] + d[i-1][2])%mod
    d[i][2] = (d[i-1][0] + d[i-1][1])%mod
print(sum(d[n])%mod)