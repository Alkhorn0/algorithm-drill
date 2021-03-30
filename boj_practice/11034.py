while True:
    try:
        l = list(map(int, input().split()))
        cnt = 0
        while True:
            if (l[2] - l[1] == 1) and (l[1] - l[0] == 1):
                break
            else:
                if l[2]-l[1] > l[1]-l[0]:
                    l[0] = l[2]-1
                    cnt += 1
                    l = sorted(l)
                else:
                    l[2] = l[0] + 1
                    cnt += 1
                    l = sorted(l)
        print(cnt)
    
    except:
        exit()