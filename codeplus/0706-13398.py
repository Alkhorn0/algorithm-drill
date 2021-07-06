# sw 역량 테스트 준비 - 기초 
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d_1 = [0]*n
d_2 = [0]*n
for i in range(n):
    d_1[i] = a[i]
    if i == 0:
        continue
    d_1[i] = max(a[i], d_1[i-1]+a[i])

for j in range(n-1, -1, -1):
    d_2[j] = a[j]
    if j == n-1:
        continue
    d_2[j] = max(a[j], d_2[j+1]+a[j])

ans = max(d_1)
for i in range(1, n-1):
    ans = max(d_1[i-1]+d_2[i+1], ans)
print(ans)