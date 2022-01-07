n = int(input())
w = list(map(int, input().split()))
ans = sum(w)

for i in range(n):
    s1 = sum(w[:i])
    s2 = sum(w[i:])
    ans = min(ans, abs(s1-s2))

print(ans)