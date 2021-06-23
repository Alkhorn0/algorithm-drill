import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x == 0:
        print(heapq.heappop(h) if len(h) != 0 else 0)
    elif x > 0:
        heapq.heappush(h, x)
