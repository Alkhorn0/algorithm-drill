# 다이나믹 프로그래밍
n = int(input())
mod = 10007
d = [[0 for _ in range(10)] for _ in range(n+1)]
d[1] = [1 for _ in range(10)]
for i in range(2, n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][:j+1])
print(sum(d[n])%mod)