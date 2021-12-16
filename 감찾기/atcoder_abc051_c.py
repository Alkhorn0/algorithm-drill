sx, sy, tx, ty = map(int, input().split())
dx = tx-sx
dy = ty-sy

ans = ''

#path1
ans += ('U'*dy+'R'*dx)
#path2
ans += ('D'*dy+'L'*dx)
#path3
ans += ('L'+'U'*(dy+1)+'R'*(dx+1)+'D')
#path4
ans += ('R'+'D'*(dy+1)+'L'*(dx+1)+'U')

print(ans)