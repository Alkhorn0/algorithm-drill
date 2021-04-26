import heapq, sys
input = sys.stdin.readline
s = []
n = int(input())
for _ in range(n):
    order = int(input())
    if order != 0:
        heapq.heappush(s,order)
    elif order == 0 and len(s) == 0:
        print(0)
    else:
        print(heapq.heappop(s))