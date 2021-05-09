# 다시보기
# 다이나믹 프로그래밍
n = int(input())
a = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
d = [[0]*3 for _ in range(n+1)]
ans = 1000*1000 + 1
for k in range(3):
    for j in range(3):
        # 마을의 형태가 원형이므로 1번과 n번이 같은 색으로 칠해지면 안되므로 미리 1번의 색을 정해두고 시작
        if j == k:
            d[1][j] = a[1][j]
        else:
            # 정한색 이외의 색이 선택되는 경우의 수를 없애기 위한 큰 수 대입
            d[1][j] = 1000*1000+1
    # 직선 마을 풀듯이 품
    for i in range(2, n+1):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]
    for j in range(3):
        # n번집과 1번집의 색의 같은 경우는 제외
        if j == k:
            continue
        ans = min(ans, d[n][j])
print(ans)