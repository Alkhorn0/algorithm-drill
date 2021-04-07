n, l = map(int,input().split())
position = list(map(int,input().split()))

position = sorted(position)

for i in range(n):
    if l < position[i]:
        break
    l += 1

print(l)