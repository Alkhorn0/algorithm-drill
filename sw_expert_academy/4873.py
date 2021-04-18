T = int(input())
for t in range(1, T+1):
    string = input()
    l = []
    for i in string:
        l.append(i)
        if len(l) == 1:
            continue
        elif l[-1] == l[-2]:
            l.pop()
            l.pop()
    print(f'#{t} {len(l)}')