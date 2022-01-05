n, m = map(int, input().split())
left, right = 0, n
for _ in range(m):
    l, r = map(int, input().split())
    left = max(l, left)
    right = min(r, right)
ans = right - left + 1
print(ans if ans > 0 else 0)