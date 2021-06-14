# sw 역량 테스트 준비 - 기초
def go(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    ans = 0
    for i in range(1, 4):
        ans += go(n-i)
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(go(n))