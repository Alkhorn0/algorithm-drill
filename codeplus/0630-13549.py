# sw 역량 테스트 준비 - 기초 
from collections import deque

n, k = map(int, input().split())
d = [-1]*(100001)
q = deque()
q.append(n)
d[n] = 0

while q:
    x = q.popleft()
    for i in [2*x, x-1, x+1]:
        if 0 <= i <= 100000:
            if d[i] != -1:
                continue
            if i == 2*x:
                d[i] = d[x]
                q.appendleft(i)
            elif i == x-1 or i == x+1:
                d[i] = d[x]+1
                q.append(i)

print(d[k])