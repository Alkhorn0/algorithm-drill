n, k = map(int, input().split())
q = []
for i in range(1,n+1):
    q.append(i)

cnt = 0
new = []
while q:
    cnt += 1
    tmp = q[0]
    q.pop(0)
    if cnt == k:
        cnt = 0
        new.append(tmp)
        continue
    q.append(tmp)

print("<",end='')
for i in new:
    if i == new[-1]:
        print(i,end='')
    else:
        print(f"{i},",end=' ')
print(">")