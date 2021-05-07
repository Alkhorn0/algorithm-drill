# 다이나믹 프로그래밍
n = int(input())
a = list(map(int, input().split()))
d = [0]*n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[i] < a[j]:
            d[i] = max(d[j]+1, d[i])
print(max(d))