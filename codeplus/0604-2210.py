a = [list(input().split()) for _ in range(5)]
ans = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def go(index, start, x, y):
    if index == 5:
        return ans.add(start)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            go(index+1, start+a[nx][ny], nx, ny)

for i in range(5):
    for j in range(5):
        go(0, a[i][j], i, j)
print(len(ans))