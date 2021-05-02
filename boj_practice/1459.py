# 그리디 
x, y, w, s = map(int, input().split())
ans = 0
if 2*w < s:
    ans = (x + y)*w
elif 2*w > 2*s:
    if (x+y) % 2 == 0:
        ans = max(x, y)*s
    else:
        ans = (max(x, y)-1)*s + w
else:
    if (x == y):
        ans = x*s
    else:
        ans = min(x, y)*s + abs(x - y)*w

print(ans)