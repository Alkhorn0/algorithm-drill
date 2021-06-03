a, b, c, x, y = map(int, input().split())
ans = a*x + b*y
for i in range(1, 100001):
    s = 2*i*c + max(0, x-i)*a + max(0, y-i)*b 
    if ans > s:
        ans = s

print(ans)