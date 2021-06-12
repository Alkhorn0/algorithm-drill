from collections import deque
move = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
ans = [False]*201
visited = [[False]*201 for _ in range(201)]
bucket = list(map(int, input().split()))
sum = bucket[2]
q = deque()
q.append((0, 0))
visited[0][0] = True
ans[bucket[2]] = True
while q:
    v = q.popleft()
    temp = [v[0], v[1], sum-v[0]-v[1]]
    for f, t in move:
        next = temp[:]
        next[t] += next[f]
        next[f] = 0
        if next[t] >= bucket[t]:
            next[f] = next[t] - bucket[t]
            next[t] = bucket[t]
        if not visited[next[0]][next[1]]:
            visited[next[0]][next[1]] = True
            q.append((next[0], next[1]))
            if next[0] == 0:
                ans[next[2]] = True
for i in range(0, bucket[2]+1):
    if ans[i]:
        print(i, end=' ')
