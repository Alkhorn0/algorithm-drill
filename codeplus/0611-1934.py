# sw 역량 테스트 준비 - 기초
def gcd(a, b):
    while a%b > 0:
        temp = a%b
        a = b
        b = temp
    return b

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    l = a*b//g
    print(l)