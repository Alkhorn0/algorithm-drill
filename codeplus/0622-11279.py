import heapq, sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x == 0:
        print(-(heapq.heappop(h)) if len(h) != 0 else 0)
    else:
        heapq.heappush(h, -x)