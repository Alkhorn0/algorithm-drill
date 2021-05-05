# 수학, 진수 변환
a, b = map(int, input().split())
m = int(input())
a_l = list(map(int, input().split()))
n = 0
l = len(a_l) - 1
for i in a_l:
    n += i*a**(l)
    l -= 1
b_l = []
while n > 0:
    b_l.append(n%b)
    n //= b
print(' '.join(map(str, b_l[::-1])))