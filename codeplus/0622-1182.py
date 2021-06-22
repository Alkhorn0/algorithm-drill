# sw 역량 테스트 준비 - 기초 
n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, 1 << n):
    temp = 0
    for j in range(n):
        if (i & (1 << j)):
            temp += a[j]
    if temp == s:
        cnt += 1
print(cnt)