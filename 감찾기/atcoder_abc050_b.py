n = int(input())
t = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    p, x = map(int, input().split())
    ans = 0
    for i in range(n):
        if i == p-1:
            ans += x
        else:
            ans += t[i]
    print(ans)