l = []
cnt = 1
while True:
    for __ in range(cnt):
        l.append(cnt)
    cnt += 1
    if len(l) >= 1000:
        break

a, b =map(int,input().split())
s = 0
for i in range(a-1, b):
    s += l[i]
print(s)