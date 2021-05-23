# bfs
from collections import deque
s = int(input())
# d는 화면과 클립보드 상태에따른 최소 소요 시간
d = [[-1]*(s+1) for _ in range(s+1)]
q = deque()
q.append((1, 0))
d[1][0] = 0
while q:
    w, c = q.popleft()
    # 연산 3가지 조작
    # 클립보드로 화면내용 복사
    if d[w][w] == -1:
        d[w][w] = d[w][c] +1
        q.append((w, w))
    # 클립보드에서 화면으로 붙여넣기
    if w+c <= s and d[w+c][c] == -1:
        d[w+c][c] = d[w][c] + 1
        q.append((w+c, c))
    # 화면에서 글자 1개 삭제
    if w-1 >= 0 and d[w-1][c] == -1:
        d[w-1][c] = d[w][c] + 1
        q.append((w-1, c))
ans = -1
for i in range(s+1):
    if d[s][i] != -1:
        if ans == -1 or ans > d[s][i]:
            ans = d[s][i]
print(ans)