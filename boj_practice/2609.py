import sys
def gcd(a,b):
    l = []
    small = min(a,b)
    for i in range(1, small+1):
        if a % i == 0 and b % i == 0: 
            l.append(i)
    return l[-1]

def lcm(a,b):
    l = []
    big = max(a,b)
    for i in range(big, a*b+1):
        if i % a == 0 and i % b == 0:
            l.append(i)
            break
    return l[0]

a, b = map(int,sys.stdin.readline().split())

print(gcd(a,b))
print(lcm(a,b))