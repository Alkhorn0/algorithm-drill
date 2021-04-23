def makeHeap(index, value):
    tree[index] = value
    if tree[index//2] > value:
        tree[index//2], tree[index] = tree[index], tree[index//2]
        index //= 2
        makeHeap(index, tree[index])

T = int(input())
for t in range(1, T+1):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    info = list(map(int, input().split()))
    index = 1
    for i in info:
        makeHeap(index, i)
        index += 1
    answer = 0
    while n > 1:
        n //= 2
        answer += tree[n]
    print(f'#{t} {answer}')
    