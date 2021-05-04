# 수학, 최소공배수, 최대공약수
from math import gcd
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    l = a*b//gcd(a,b)
    print(l)