# 자료구조(우선순위 큐), 그리디
import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)
for _ in range(m):
    card1 = heapq.heappop(a)
    card2 = heapq.heappop(a)

    heapq.heappush(a, card1 + card2)
    heapq.heappush(a, card1 + card2)

print(sum(a))