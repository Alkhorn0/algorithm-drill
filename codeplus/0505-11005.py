# 수학, 진수 변환
n, b = map(int, input().split())
x = 0
while b**(x) <= n:
    x += 1
ans = '' 
for i in range(x):
    r = n % b
    n //= b
    if r > 9:
        ans += chr(r-10+ord('A'))
    else:
        ans += str(r)
print(ans[::-1])
