import sys, heapq
input = sys.stdin.readline

n = int(input())
r = []
l = []
for _ in range(n):
    x = int(input())
    if l == [] or r == []:
        heapq.heappush(l, -x)
    else:
        if -(l[0]) >= x:
            heapq.heappush(l, -x)
        elif r[0] <= x:
            heapq.heappush(r, x)
        else:
            heapq.heappush(l, -x)
    while not (len(l) == len(r) or len(l) == len(r)+1):
        if len(l) > len(r):
            heapq.heappush(r, -heapq.heappop(l))
        else:
            heapq.heappush(l, -heapq.heappop(r))

    sys.stdout.write(f'{-(l[0])}\n')
