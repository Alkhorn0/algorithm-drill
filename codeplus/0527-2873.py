# 틀린문제, 다시보기
r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
s = ''
if r%2 == 1:
    for i in range(r):
        if i%2 == 0:
            s += 'R'*(c-1)
            if i != r-1:
                s += 'D'
        else:
            s += 'L'*(c-1)
            s += 'D'
elif c%2 == 1:
    for j in range(c):
        if j%2 == 0:
            s += 'D'*(r-1)
            if j != c-1:
                s += 'R'
        else:
            s += 'U'*(r-1)
            s += 'R'
else:
    n = 1000
    x, y = -1, -1
    for i in range(r):
        for j in range(c):
            if (((i+j)%2 != 0) and (n > a[i][j])):
                n = a[i][j]
                x = i
                y = j
    sx,sy = 0, 0
    ex,ey = r-1, c-1
    s2 = ''
    while (ex-sx > 1):
        if sx//2 < x//2:
            s += 'R'*(c-1)
            s += 'D'
            s += 'L'*(c-1)
            s += 'D'
            sx += 2
        if x//2 < ex//2:
            s2 += 'R'*(c-1)
            s2 += 'D'
            s2 += 'L'*(c-1)
            s2 += 'D'
            ex -= 2
    
    while (ey-sy > 1):
        if sy//2 < y//2:
            s += 'D'
            s += 'R'
            s += 'U'
            s += 'R'
            sy += 1
        if y//2 < ey//2:
            s2 += 'D'
            s2 += 'R'
            s2 += 'U'
            s2 += 'R'
            ey -= 2
    
    if y == sy:
        s += 'R'
        s += 'D'
    else:
        s += 'D'
        s += 'R'
    s2 = s2[::-1]
    s += s2
print(s)