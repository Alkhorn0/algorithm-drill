# r과 c가 모두 짝수가 나온경우가 중요
r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
ans = ''
if r%2 == 1:
    while r > 0:
        if r % 2 == 1:
            ans += 'R'*(c-1)
        else:
            ans += 'L'*(c-1)
        r -= 1
        if r > 0:
            ans += 'D'
elif c%2 == 1:
    while c > 0:
        if c % 2 == 1:
            ans += 'D'*(r-1)
        else:
            ans += 'U'*(r-1)
        c -= 1
        if c > 0:
            ans += 'R' 
else:
    # 행복도가 가장 작은 타일 찾기(방문 제외할 타일)
    # 단, i+j가 홀수인 경우에 한함
    # 가장 처음에 나오는 (i+j)가 홀수인 경우
    x = 0
    y = 1
    for i in range(r):
        for j in range(c):
            if (i+j)%2 == 1:
                if a[i][j] < a[x][y]:
                    x = i
                    y = j
    x1 = 0
    y1 = 0
    x2 = r-1
    y2 = c-1
    rev = ''
    # 방문 안할 타일주위 2*2 영역을 제외한 부분은 
    # R->D->L->D 순으로 반복
    while x2-x1 > 1:
        if (x1//2 < x//2):
            ans += 'R'*(c-1)
            ans += 'D'
            ans += 'L'*(c-1)
            ans += 'D'
            x1 += 2
        # 아래에서부터 올라오는 경우는 반대로 읽을 수 있도록 함
        if (x//2 < x2//2):
            rev += 'R'*(c-1)
            rev += 'D'
            rev += 'L'*(c-1)
            rev += 'D'
            x2 -= 2
    # 제외할 타일이 있는 2*m영역은 D->R->U->R로 반복 
    while y2-y1 > 1:
        if (y1//2 < y//2):
            ans += 'D'
            ans += 'R'
            ans += 'U'
            ans += 'R'
            y1 += 2
        # 제외할 타일을 지나간경우는 R->U->R->D 이므로 
        # 위와 같은 방법으로 받아서 뒤집으면 됨
        if (y//2 < y2//2):
            rev += 'D'
            rev += 'R'
            rev += 'U'
            rev += 'R'
            y2 -= 2
    # 제외할 타일은 지나가지 않도록 한다
    # 2*2 까지 줄였을때 해당 타일이 (1, 0)의 경우
    if y == y1:
        ans += 'R'
        ans += 'D'
    # (0, 1)의 경우
    else:
        ans += 'D'
        ans += 'R'
    ans += rev[::-1]
print(ans)