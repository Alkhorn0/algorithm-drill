from heapq import heappop, heappush

n, q = map(int, input().split())
event = []

for _ in range(n):
    s, t, x = map(int, input().split())
    event.append([s-x, x, t-x])
event.sort()

used = 0
hq = []
for _ in range(q):
    d = int(input())
    while used < n:
        if event[used][0] <= d:
            heappush(hq, (event[used][1], event[used][2]))
            used += 1
        else:
            break
    ans = -1
    while hq:
        x, t = heappop(hq)
        if d < t:
            ans = x
            heappush(hq, (x, t))
            break
    print(ans)