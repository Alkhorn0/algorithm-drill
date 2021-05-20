# 다시보기
# 13460번과 비슷하지만 무의미한 이동이 없음 -> 이동 시 줄일 경우의 수 없음
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
LIMIT = 5

# 4방향이동이므로 2진법->4진법으로 진법변환
def gen(k):
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] = (k&3)
        k >>= 2
    return a

# 이동 결과 / 주의점으로는 이동시 같은 수가 있으면 병합되는데 이는 이동방향에 우선함 
# 예를 들어 좌로 이동시 2022가 일렬로 있으면 4200가 된다는 말
def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a]

    for dir in dirs:
        ok = False
        # 직전에 병합된 적이 있는 지 여부 (직전에 병합됐으면 바로 병합 못 시킴)
        merged = [[False]*n for _ in range(n)]

        # 이동 0-> 아래/ 1-> 위/ 2-> 왼쪽/ 3-> 오른쪽/ 한 칸씩 차례로 이동
        # 이동 시킬 칸이 숫자가 있는지 판단
        # 이동하려는 칸에 숫자가 있는지 판단후 없으면 그대로 정보 이동
        # 이동하려는 칸에 숫자가 있고 같은 숫자면, 병합진행 숫자 *2 원래 좌표에 0대입
        while True:
            # 이동가능한 칸이 있는지 판단(while문 탈출을 위한도구)
            ok = False
            if dir == 0:
                for i in range(n-2, -1, -1):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i+1][j] == 0:
                            d[i+1][j] = d[i][j]
                            merged[i+1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i+1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i+1][j]:
                                d[i+1][j] *= 2
                                merged[i+1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 1:
                for i in range(1, n):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i-1][j] == 0:
                            d[i-1][j] = d[i][j]
                            merged[i-1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i-1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i-1][j]:
                                d[i-1][j] *= 2
                                merged[i-1][j] = True
                                d[i][j] = 0
                                ok = True
            
            elif dir == 2:
                for j in range(1, n):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j-1] == 0:
                            d[i][j-1] = d[i][j]
                            merged[i][j-1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j-1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j-1]:
                                d[i][j-1] *= 2
                                merged[i][j-1] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 3:
                for j in range(n-2, -1, -1):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j+1] == 0:
                            d[i][j+1] = d[i][j]
                            merged[i][j+1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j+1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j+1]:
                                d[i][j+1] *= 2
                                merged[i][j+1] = True
                                d[i][j] = 0
                                ok = True
            
            if not ok:
                break
    # 가장 큰 수 찾아서 반환
    ans = max([max(row) for row in d])
    return ans

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 모든 이동하는 경우의 수 대입
for k in range(1 << (LIMIT*2)):
    dirs = gen(k)
    # 이동결과로 나온 가장 큰 수 판단(더 큰 수가 필요)
    cur = check(a, dirs)
    if ans < cur:
        ans = cur
print(ans)