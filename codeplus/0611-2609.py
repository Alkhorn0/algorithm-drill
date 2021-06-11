# sw 역량 테스트 준비 - 기초
a, b = map(int, input().split())
def gcd(a, b):
    while a % b > 0:
        temp = a%b
        a = b
        b = temp
    return b
g = gcd(a, b)
l = a*b//g
print(g)
print(l)


    