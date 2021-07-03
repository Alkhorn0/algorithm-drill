# sw 역량 테스트 준비 - 기초 
d = [0]*(1000001)
d[1] = 1
d[2] = 2
d[3] = 4
mod = 1000000009
for i in range(4, 1000000+1):
    d[i] = (d[i-3]+d[i-2]+d[i-1])%mod
T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])