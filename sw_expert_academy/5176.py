def makeTree(index):
    global count
    if index <= n:
        makeTree(index*2)
        tree[index] = count
        count += 1
        makeTree(index*2 + 1)
T = int(input())
for t in range(1,T+1):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    count = 1
    makeTree(1)
    print(f'#{t} {tree[1]} {tree[n//2]}')