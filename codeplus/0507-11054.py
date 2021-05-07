# 다시보기
# 다이나믹 프로그래밍
n = int(input())
a = list(map(int, input().split()))
d1 = [0]*n
d2 = [0]*n
for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            d1[i] = max(d1[j]+1, d1[i])
for i in range(n-1, -1, -1):
    d2[i] = 1
    for j in range(i+1, n):
        if a[i] > a[j]:
            d2[i] = max(d2[j]+1, d2[i])
d = [d1[i]+d2[i]-1 for i in range(n)]
print(max(d))