T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    answer = []
    for i in range(5):
        answer.append(a[-(i+1)])
        answer.append(a[i])
    print(f'#{t}',end=' ')
    for i in answer:
        print(i, end=' ')
    print()