# sw 역량 테스트 준비 - 기초
def gcd(a, b):
    while a%b > 0:
        temp = a%b
        a = b
        b = temp
    return b

t = int(input())
for _ in range(t):
    n, *a = map(int, input().split())
    gcds = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            gcds.append(gcd(a[i], a[j]))
    print(sum(gcds))