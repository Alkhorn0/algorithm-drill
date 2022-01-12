h, w = map(int, input().split())
if h%3 == 0 or w%3 == 0:
    ans = 0
else:
    ans = 10**16
if h > 3: ans = min(ans, w)
if w > 3: ans = min(ans, h)

x = w // 2
for i in range(1, h):
    a = i * w
    b = (h - i) * x
    c = (h - i) * (w - x)
    ans = min(ans, max(a, b, c) - min(a, b, c))
y = h // 2
for i in range(1, w):
    a = i * h
    b = (w - i) * y
    c = (w - i) * (h - y)
    ans = min(ans, max(a, b, c) - min(a, b, c))
print(ans)