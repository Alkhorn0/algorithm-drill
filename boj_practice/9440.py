while True:
    line = list(map(int,input().split()))
    if line[0] == 0:
        break
    q = line[1:]
    q = sorted(q)
    
    zero_count = 0
    if q[0] == 0:
        for i in q:
            if i != 0:
                break
            zero_count += 1
        tmp = q[0]
        q[0] = q[zero_count]
        q[zero_count] = tmp
        tmp = q[1]
        q[1] = q[zero_count + 1]
        q[zero_count + 1] = tmp
    #print(q)

    
    a, b = "", ""
    for i in range(len(q)):
        if i % 2 == 0:
            a += str(q[i])
        else:
            b += str(q[i])

    print(int(a)+int(b))