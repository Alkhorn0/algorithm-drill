# bfs
# 어짜피 뱀이던, 사다리던 x -> y로 이동은 같음
# 때문에 구분할 필요 X
# 다른 bfs시뮬레이션 문제와 동일하게 이동시키며 해결함
from collections import deque

n, m = map(int, input().split())
go = list(range(101))
# 이전에 방문했는지 확인 겸 주사위 몇번으로 올 수 있는지를 기록
d = [-1]*101
for _ in range(n+m):
    x, y = map(int, input().split())
    go[x] = y
d[1] = 0
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1, 7):
        nx = x+i
        if nx > 100:
            continue
        nx = go[nx]
        # 방문한 적 없으면 d에 추가하고 q에도 추가
        if d[nx] == -1:
            d[nx] = d[x] + 1
            q.append(nx)
print(d[100])