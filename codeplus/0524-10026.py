from collections import deque

n = int(input())
a = [input() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# blind = 적록색약여부 , u,v = 좌표에 칠해진 색
# can -> 같은 색인지 아닌지 판정하는 함수
def can(blind, u, v):
    # 두 정점의 색이 같은 경우 -> True
    if u == v:
        return True
    # 정점의 색은 다르지만 적록색약의 경우 
    # R과 G를 구분할 수 없으니 같은 것으로 처리
    if blind:
        if u == 'R' and v == 'G':
            return True
        if u == 'G' and v == 'R':
            return True
    # 나머지는 같지 않음
    return False

# 입력받은 판의 상태와 색약의 여부를 인자로 받음
def go(a, blind):
    n = len(a)
    # 방문 여부 
    visited = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            # 방문 여부 확인 -> 있으면 제외
            if visited[i][j]:
                continue
            # 새롭게 방문할때마다 증가
            ans += 1
            # bfs
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 방문 기록 확인
                        if visited[nx][ny]:
                            continue
                        # 색 구분 
                        if can(blind, a[x][y], a[nx][ny]):
                            visited[nx][ny] = True
                            q.append((nx, ny))
    # ans는 증가만 하므로 구분한 지역의 갯수를 뜻 함
    return ans

normal = go(a, False)
blind = go(a, True)
print(normal, blind)