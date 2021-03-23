d = []                  # 빈 리스트 생성
for i in range(20):
    d.append([])        # 리스트 안에 새로운 리스트 추가
    for j in range(20):
        d[i].append(0)  # 리스트 안에 들어있는 리스트에 0 추가

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')     # 공백을 두고 한 줄로 출력
    print()                         # 줄 바꿈