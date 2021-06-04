c, p = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
if p == 1:
    for i in range(c):
        cnt += 1
    for i in range(c):
        if i+3 >= c:
            break
        if a[i]+1 == a[i+1]+1 == a[i+2]+1 == a[i+3]+1:
            cnt += 1
elif p == 2:
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+2 == a[i+1]+2:
            cnt += 1
elif p == 3:
    for i in range(c):
        if i+2 >= c: 
            break
        if a[i]+1 == a[i+1]+1 and a[i+1]+2 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+1 == a[i+1]+2:
            cnt += 1
elif p == 4:
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+1 == a[i+1]+2 and a[i+1]+1 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+2 == a[i+1]+1:
            cnt += 1
elif p == 5:
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+1 == a[i+1]+1 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+2 == a[i+1]+1:
            cnt += 1
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+1 == a[i+1]+2 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+1 == a[i+1]+2:
            cnt += 1
elif p == 6:
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+1 == a[i+1]+1 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+1 == a[i+1]+1:
            cnt += 1
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+2 == a[i+1]+1 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+1 == a[i+1]+3:
            cnt += 1
elif p == 7:
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+1 == a[i+1]+1 == a[i+2]+1:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+3 == a[i+1]+1:
            cnt += 1
    for i in range(c):
        if i+2 >= c:
            break
        if a[i]+1 == a[i+1]+1 == a[i+2]+2:
            cnt += 1
    for i in range(c):
        if i+1 >= c:
            break
        if a[i]+1 == a[i+1]+1:
            cnt += 1
print(cnt)