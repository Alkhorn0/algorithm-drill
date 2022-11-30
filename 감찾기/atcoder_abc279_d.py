import math

a, b = map(int, input().split())
t = int((a/(2*b))**(2/3)-1)

ans = float('inf')
for x in range(max(0, t-100), t+100):
    ans = min(b*x+a/math.sqrt(1+x), ans)
print(ans)