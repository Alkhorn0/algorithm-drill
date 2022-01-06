n = int(input())
ans = []
for i in range(n):
    s, p = input().split()
    ans.append((s, -int(p), i+1))

ans.sort()

for s, p, i in ans:
    print(i)