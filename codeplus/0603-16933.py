# 0602의 개선
# 4차원배열 -> 2차원배열 줄임
# 큐에는 좌표와 바위를 깰 수 있는 횟수, 이동횟수, 낮과밤 여부를 저장
# 이전에는 위의 요소를 배열의 차원을 늘리며 담았지만,
# 시간을 줄이기위해 계산만 해서 큐에 추가한다
# 이동횟수를 dist에 기록하여 목적지에 도착한 경우 중에 최소횟수를 찾는 방법만 생각했지만,
# 어떻게 더 적은 경우를 q에 추가할지를 고려해야 할 듯
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [input() for _ in range(n)]
# 각 칸마다 남은 바위를 깨는 횟수 저장
dist = [[-1]*m for _ in range(n)]
q = deque()
# 목적지까지 가는데 걸린 횟수의 최소값 저장
answer = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q.append((0, 0, k, 1, 1))
while q:
    x, y, z, count, day = q.popleft()
    # 목적지 도착한 경우, 처음 도착햇거나, 행한 시행중
    # 더 적은 이동횟수를 가지는 경우가 있으면 갱신해줌
    if (x, y) == (n-1, m-1):
        if answer == -1 or answer > count:
            answer = count
        continue
    # dist에 바위를 깰 수있는 횟수를 저장하는게 특징
    # 바위를 더 적게 깨는 경우로 갱신해줌(dist값이 작은 경우 -> 바위를 많이 깬 경우)
    # z가 dist보다 큰 경우-> 바위를 덜 깨고 간 것
    # 바위를 많이 깨고 온 경우 돌아왔을 수도 있으므로 경우를 줄여주는 역할가능할 듯(?)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 바위는 낮에만 깰 수 있음
            if a[nx][ny] == '1' and day:
                # 방문한 적이 없거나 더 적은 횟수의 바위를 깨고 온경우
                if dist[nx][ny] < z-1:
                    dist[nx][ny] = z-1
                    q.append((nx, ny, z-1, count+1, 0))
            elif a[nx][ny] == '0':
                if dist[nx][ny] < z:
                    dist[nx][ny] = z
                    q.append((nx, ny, z, count+1, 1-day))
    # 바위를 깨지 않고는 이동하지 못할 경우 한번 쉬고 이동가능하므로
    # 그 경우의 추가
    if not day:
        q.append((x, y, z, count+1, 1-day))
print(answer)