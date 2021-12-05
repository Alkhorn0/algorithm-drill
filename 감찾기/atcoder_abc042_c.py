n, k = map(int, input().split())
d = list(map(int, input().split()))

while(True):
    s = str(n)
    p = 0
    for j in s:
        if int(j) in d:
            p = 1
            break
    if p == 1:
        n += 1
    else:
        print(n)
        break