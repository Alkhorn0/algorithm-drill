m, k = map(int, input().split())
if 2**m-1 < k:
    print(-1)
    exit()
if m == 1:
    if k == 0:
        print('0 0 1 1')
        exit()
    else:
        print(-1)
        exit()

b = []
for i in range(2**m):
    if i == k:
        continue
    b.append(i)
c = b[::-1]

for i in b:
    print(i, end=' ')
print(k, end=' ')
for j in c:
    print(j, end=' ')
print(k, end=' ')