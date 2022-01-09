n = int(input())
a = list(map(int, input().split()))
ans = 10**18

for p in (1, -1):
    s = 0
    cost = 0
    for ai in a:
        s += ai
        if p * s >= 0:
            cost += abs(s) + 1
            s = -p
        p *= -1
    ans = min(cost, ans)

print(ans)