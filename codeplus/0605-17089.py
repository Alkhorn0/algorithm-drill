# 친구관계 = 연결성분 -> 그래프문제
n, m = map(int, input().split())
# 친구관계 == 연결됨
a = [[False]*(n+1) for _ in range(n+1)]
# 친구관계를 가진 사람 수
d = [0]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = a[y][x] = True
    d[x] += 1
    d[y] += 1

ans = -1

for i in range(1, n+1):
    for j in range(1, n+1):
        # i와 j가 친구일때 새로운 친구를 찾는다
        if a[i][j]:
            for k in range(1, n+1):
                if a[i][k] and a[j][k]:
                    # 서로에대한 친구관계는 빼고 계산하므로 -6
                    s = d[i]+d[j]+d[k]-6
                    if ans == -1 or ans > s:
                        ans = s
print(ans)