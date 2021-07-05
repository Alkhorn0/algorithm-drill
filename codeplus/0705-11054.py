# sw 역량 테스트 준비 - 기초 
n = int(input())
a = list(map(int, input().split()))
d_1 = [0]*n
d_2 = [0]*n

for i in range(n):
    d_1[i] = 1
    for j in range(i):
        if a[j] < a[i] and d_1[i] < d_1[j]+1:
            d_1[i] = d_1[j]+1
for i in range(n-1, -1, -1):
    d_2[i] = 1
    for j in range(n-1, i-1, -1):
        if a[j] < a[i] and d_2[i] < d_2[j]+1:
            d_2[i] = d_2[j]+1

ans = 0
for k in range(n):
    if ans < d_1[k]+d_2[k]-1:
        ans = d_1[k]+d_2[k]-1
print(ans)