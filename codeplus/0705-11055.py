# sw 역량 테스트 준비 - 기초 
n = int(input())
a = list(map(int, input().split()))
d = [0]*n

for i in range(n):
    d[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j]+a[i]:
            d[i] = d[j]+a[i]

print(max(d))
print(d)