# sw 역량 테스트 준비 - 기초
prime = [True]*1001
prime[1] = False
for i in range(2, 1001):
    if not prime[i]:
        continue
    j = 2
    while i*j <= 1000:
        prime[i*j] = False
        j += 1

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if prime[i]:
        ans += 1
print(ans) 