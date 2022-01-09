import heapq
n, k = map(int, input().split())
p = list(map(int, input().split()))

que = p[0:k]
print(min(que))
heapq.heapify(que)

for i in range(k, n):
    #print(que)
    m = heapq.heappop(que)
    m = max(m, p[i])
    heapq.heappush(que, m)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)