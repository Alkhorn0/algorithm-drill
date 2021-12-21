n = int(input())
s = input()
p = ['SS','SW','WS','WW']

for i in p:
    for j in range(1, n-1):
        if i[j] == 'S':
            if s[j] == 'o':
                if i[j-1] == 'S':
                    i += 'S'
                else:
                    i += 'W'
            else:
                if i[j-1] == 'S':
                    i += 'W'
                else:
                    i += 'S'
        else:
            if s[j] == 'o':
                if i[j-1] == 'S':
                    i += 'W'
                else:
                    i += 'S'
            else:
                if i[j-1] == 'S':
                    i += 'S'
                else:
                    i += 'W'
    flag = True
    if i[n-1] == 'S':
        if s[n-1] == 'o':
            if i[n-2] == i[0]:
                flag = True
            else:
                flag = False
        else:
            if i[n-2] != i[0]:
                flag = True
            else:
                flag = False
    else:
        if s[n-1] == 'o':
            if i[n-2] != i[0]:
                flag = True
            else:
                flag = False
        else:
            if i[n-2] == i[0]:
                flag = True
            else:
                flag = False
    if not flag:
        continue

    if i[0] == 'S':
        if s[0] == 'o':
            if i[n-1] == i[1]:
                flag = True
            else:
                flag = False
        else:
            if i[n-1] != i[1]:
                flag = True
            else:
                flag = False
    else:
        if s[0] == 'o':
            if i[n-1] != i[1]:
                flag = True
            else:
                flag = False
        else:
            if i[n-1] == i[1]:
                flag = True
            else:
                flag = False
    
    if flag:
        print(i)
        exit()
print(-1)
    
