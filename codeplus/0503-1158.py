# 다시보기
# 자료구조, 큐
from collections import deque

n, k = map(int, input().split())
q = deque()
for i in range(1, n+1):
    q.append(i)
ans = []
for i in range(n-1):
    for j in range(k-1):
        q.append(q.popleft())
    ans += [q.popleft()]
ans += [q[0]]
print('<'+', '.join(map(str, ans)) + '>')