# 완전 탐색 문제
r, b = map(int,input().split())
l,w = 0, 0
for i in range(3, 2000):
    for j in range(3, 2000):
        if r == 2*i + 2*j - 4 and i*j == r+b:
            if i != j:
                l = max(i,j)
                w = min(i,j)
            else:
                l, w = i, j
            break
print(l,w)
