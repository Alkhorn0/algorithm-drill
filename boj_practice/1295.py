while True:
    n = input()
    if n == '0':
        break
    else:
        l,palindrom,cnt = [], [], 0
        for i in n:
            l.append(i)
        for j in range(len(l)-1,-1,-1):
            palindrom.append(l[j])
        for k in range(len(l)//2):
            if palindrom[k] == l[k]:
                cnt += 1
        
        if cnt == len(l)//2:
            print('yes')
        else:
            print('no')

        