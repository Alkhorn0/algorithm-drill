n = int(input())
march = [0, 0, 0, 0, 0]
for _ in range(n):
    si = input()
    if si[0] == 'M':
        march[0] += 1
    elif si[0] == 'A':
        march[1] += 1
    elif si[0] == 'R':
        march[2] += 1
    elif  si[0] == 'C':
        march[3] += 1
    elif si[0] == 'H':
        march[4] += 1
ans = 0
com = [(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(0,3,4),(1,2,3),(1,2,4),(1,3,4),(2,3,4)]
for i, j, k in com:
    ans += march[i]*march[j]*march[k]
print(ans)