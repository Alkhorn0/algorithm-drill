p, q, r = map(int, input().split())

ans = min(p + q, q + r, r + p)
print(ans)