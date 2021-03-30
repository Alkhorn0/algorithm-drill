n = int(input())
l = []
for __ in range(n):
    d = int(input())
    if len(l) == 0:
        l.append(d)
    else:
        for j in range(len(l)):
            if d == l[j]:
                break
            elif d != l[j] and j == len(l) - 1:
                l.append(d)
print(len(l))
            
