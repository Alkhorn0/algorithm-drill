# 다이나믹 프로그래밍
n = int(input())
a = list(map(int, input().split()))
d = [0]*n
for i in range(n):
    d[i] = a[i]
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + a[i])
print(max(d))