T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())
    tree = [0 for _ in range(n+1)]
    for _ in range(m):
        index, value = map(int, input().split())
        tree[index] = value
    if n%2 == 0:
        tree[n-m] = tree[n]
        for i in range(n-m-1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]
            if i == l:
                print(f'#{t} {tree[l]}')
                break
    else:        
        for i in range(n-m, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]
            if i == l:
                print(f'#{t} {tree[l]}')
                break