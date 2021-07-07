# sw 역량 테스트 준비 - 기초 
n = int(input())
m = int(input())
broken = [False]*10
if m > 0:
    a = list(map(int, input().split()))
else:
    a = []
for i in a:
    broken[i] = True

def possible(i):
    if i == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while i > 0:
        if broken[i%10]:
            return 0
        l += 1
        i //= 10
    return l

ans = abs(n-100)
for i in range(1000001):
    l = possible(i)
    if l > 0:
        press = abs(i-n)
        if ans > l+press:
            ans = l+press
print(ans)