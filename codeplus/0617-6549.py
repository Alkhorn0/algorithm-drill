# 다시보기
while True:
    n, *l = list(map(int, input().split()))
    if n == 0:
        break
    s = []
    ans = 0

    l.append(0)
    for i, h in enumerate(l):
        while s and l[s[-1]] > h:
            
            height = l[s.pop()]
            if s:
                width = i-s[-1]-1
            else:
                width = i
                
            if ans < width*height:
                ans = width*height
        s.append(i)
    print(ans)