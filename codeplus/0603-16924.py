# 다시보기
# 모든 '*' 가 십자가의 중앙이라고 생각하고 십자가를 그려봄

n, m = map(int, input().split())
a = [input() for _ in range(n)]
# 십자가로 표현가능한 경우인지 판정을 위함
check = [[False]*m for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        # '*'인 칸을 찾아서, k -> 낮은수부터 차차 올려 
        # 만들 수 있는 최대 십자가 크기를 구하기 위해 사용
        # l -> 만들 수 있는 십자가 크기 저장
        if a[i][j] == '*':
            l = 0
            k = 1
            # 만들수 있는 십자가의 최대 크기를 구한다
            while True:
                # 십자가는 상하좌우에 '*'을 가짐
                # 격자판 바깥으로 나가는 경우는 제외해야함
                if i+k < n and i-k >= 0 and j+k < m and j-k >= 0:
                    # 십자가의 조건을 만족하면 l을 갱신
                    if a[i+k][j] == '*' and a[i-k][j] == '*' and a[i][j-k] == '*' and a[i][j+k] == '*':
                        l = k
                    else:
                        break
                else:
                    break
                k += 1
            # 십자가의 중심이 될 수 있는 좌표는 저장
            if l > 0:
                ans.append((i+1, j+1, l))
                check[i][j] = True
                for k in range(1, l+1):
                    check[i+k][j] = True
                    check[i-k][j] = True
                    check[i][j-k] = True
                    check[i][j+k] = True

for i in range(n):
    for j in range(m):
        # '*'이지만 십자가로 만들 수 없는 좌표가 있는 경우 만들 수 없는 격자판
        if a[i][j] == '*' and check[i][j] == False:
            print(-1)
            exit()
print(len(ans))
for i in ans:
    print(' '.join(map(str, i)))