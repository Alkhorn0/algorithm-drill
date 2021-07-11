# sw 역량 테스트 준비 - 기초 
n = int(input())
ans = 0
s = 1
l = 1
while s <= n:
    e = s*10-1
    if e > n:
        e = n
    ans += (e-s+1)*l
    s *= 10
    l += 1
print(ans)